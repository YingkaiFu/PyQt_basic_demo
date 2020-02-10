# encoding:utf-8
import os
import re
import sqlite3
import sys
import threading
from datetime import datetime
from datetime import timedelta

import cv2
import numpy as np
import qdarkstyle
import yaml
from PIL import ImageGrab
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QUrl, Qt, QCoreApplication
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import *

from ui_file_manager import Ui_File_Browser as Ui_Show_file
from ui_login import Ui_dialog as Ui_Login
from ui_main import Ui_MainWindow as Ui_Main
from ui_reset import Ui_Dialog as Ui_Reset


def get_yaml_data(yaml_file):
    return yaml.load(open(yaml_file, 'r', encoding="utf-8").read(), Loader=yaml.FullLoader)


yaml_path = os.path.join(os.getcwd(), "config.yaml")
DATA = get_yaml_data(yaml_path)

capture_path = os.path.join(os.getcwd(), DATA["LOCAL"]["SCREEN_DIR"])
download_dir = os.path.join(os.getcwd(), DATA["LOCAL"]["DOWNLOAD_DIR"])
remote_file_path = '/home/' + DATA["REMOTE"]["USERNAME"] + '/' + DATA["REMOTE"]["VIDEO_FILE_PATH"]
FILE_SYS = ['mmcb', 'root', 'home']
file_sys = FILE_SYS[int(DATA["REMOTE"]["FILE_SYSTEM"])]

if not os.path.exists(capture_path):
    os.makedirs(capture_path)
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
database = 'userdata.db'

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True, start_kb=False):
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    if start_kb:
        size = size * multiple
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


def check_ip(ipAddr):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|['
        '1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False


def show_box(title, message):
    ok = QtWidgets.QPushButton()
    msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, title, message)
    msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
    ok.setText(u'确定')
    msg.exec_()


class Main(QMainWindow):
    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        icon = QtGui.QIcon("favicon.ico")
        self.setWindowIcon(icon)
        self.download_windows = File_Manager()

        self.date = datetime.fromisoformat('2011-11-04T00:00:00')
        self.state = True
        self.ui.time.setText(self.date.strftime('%H:%M:%S'))

        self.ui.dialog.clicked.connect(self.show_dialog)
        self.ui.video.clicked.connect(self.on_video)
        self.ui.file.clicked.connect(self.file_browser)
        self.ui.set_ip.clicked.connect(self.set_ip)
        self.ui.file_2.clicked.connect(self.show_files)

        self.record_state = QTimer()
        self.record_state.setInterval(1000)
        self.record_state.timeout.connect(self.onTimerOut)
        self.runing_state = QTimer()
        self.runing_state.setInterval(1000)
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    def show_files(self):
        self.download_windows.show()

    def on_video(self):
        if self.state:
            self.date = datetime.fromisoformat('2011-11-04T00:00:00')
            self.ui.video.setText("Stop")
            self.record_state.start()
            th = threading.Thread(target=self.on_event)
            th.start()
            self.state = False
        else:
            self.ui.video.setText("Screen recorder")

            self.stopEvent.set()
            self.record_state.stop()
            self.state = True

    def onTimerOut(self):

        self.date = self.date + timedelta(seconds=1)
        self.ui.time.setText(self.date.strftime('%H:%M:%S'))

    def on_event(self):

        screen = ImageGrab.grab()
        now = datetime.now()
        filename = now.strftime("%Y%m%d%H%M%S") + '.avi'
        length, width = screen.size
        video_decode_style = cv2.VideoWriter_fourcc(*'XVID')
        video = cv2.VideoWriter(os.path.join(capture_path, filename), video_decode_style, 8, (length, width))
        while True:
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            video.write(imm)

            if self.stopEvent.is_set():
                self.record_state.stop()
                self.stopEvent.clear()
                break
        video.release()
        cv2.destroyAllWindows()

    def file_browser(self):

        QDesktopServices.openUrl(QUrl('file:///' + capture_path))

    def set_ip(self):

        text, ok = QInputDialog.getText(self, 'Input ip', 'input ip:')
        if ok:
            if check_ip(str(text)):
                self.ip = str(text)
                global  used_ip
                used_ip = self.ip
                self.ui.ip.setText(str(text))
            else:
                show_box("Setting Error", "IP not valid")

    def show_dialog(self):
        show_box("失败", "First")

class File_Manager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Show_file()
        self.ui.setupUi(self)
        self.ui.tableWidget.setHorizontalHeaderLabels(['File name', 'Size(MB)'])
        icon = QtGui.QIcon("favicon.ico")
        self.setWindowIcon(icon)
        self.current_file = None
        self.current_file_size = None
        self.downloading = False

        self.ui.fetch_data.clicked.connect(self.update_table)
        self.ui.tableWidget.itemClicked.connect(self.handleItemClick)
        self.ui.delete_file.clicked.connect(self.delete)

    def delete(self):
        """
        点击"删除"按钮事件，该事件根据表格中的选中文件，使用Pramiko来删除该文件，并重新更新表格
        :return:
        """
        if self.current_file is None:
            show_box("删除", '请选中需要删除的文件')
        else:
            file = os.path.join(os.getcwd(), self.current_file)
            os.remove(file)

    def handleItemClick(self, item):
        """
        点击表格内容的响应事件，该事件根据表格中所选中文件，来设置current_file
        :param item: 点击的位置
        :return:
        """
        row_num = -1
        for i in self.ui.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        self.current_file = self.ui.tableWidget.item(row_num, 0).text()
        self.current_file_size = self.ui.tableWidget.item(row_num, 1).text()

    def update_table(self):
        """
        刷新表格，首先读取开发板上文件夹下的所有文件属性，将其文件名和大小设置到界面上的表格中，并按照文件名降序进行排序，
        之后使用paramiko读取home目录下的空间总量和剩余空间量并显示在文件管理界面上
        :return:
        """

        file_name_list = []
        file_size_list = []

        state_list = (os.listdir(os.getcwd()))
        print(state_list)
        num = 0
        for file in state_list:
            if os.path.isfile(file):
                file_name_list.append(file)
                file_size_list.append(os.stat(file).st_size)
                num = num + 1
        self.ui.tableWidget.setRowCount(num)
        for i in range(num):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(file_name_list[i])))
            size = approximate_size(int(str(file_size_list[i])), a_kilobyte_is_1024_bytes=False)
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(size)))
        self.ui.tableWidget.sortItems(0, Qt.DescendingOrder)


class Login(QDialog):
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        icon = QtGui.QIcon("favicon.ico")
        self.setWindowIcon(icon)
        self.main_window = Main()
        self.reset_window = Reset()

        self.ui.sign_in.clicked.connect(self.show_main)
        self.ui.reset.clicked.connect(self.show_reset)

    def show_main(self):
        warning = self.check_account()
        if warning is None:
            self.hide()
            self.main_window.show()
        else:
            show_box("Login error", warning)

    def showdata(self, id):
        conn = sqlite3.connect(database)
        data = conn.execute("select PASSWORD from USER where ID='%s'" % id).fetchone()
        conn.close()
        return data

    def check_account(self):
        id = 'admin'
        pw = self.ui.password.text()
        data = self.showdata(id)
        if data:
            if data[0] == pw:
                return None
            else:
                warning = "Check your password"
                return warning
        else:
            warning = "No such user"
            return warning

    def show_reset(self):
        self.reset_window.show()


class Reset(QDialog):
    def __init__(self, *args):
        super().__init__(*args)
        self.ui = Ui_Reset()
        self.ui.setupUi(self)
        icon = QtGui.QIcon("favicon.ico")
        self.setWindowIcon(icon)
        self.id = 'admin'
        self.message = None

        self.ui.yes.clicked.connect(self.save)
        self.ui.no.clicked.connect(self.close)

    def save(self):
        origin = self.ui.pre_password.text()
        new = self.ui.password.text()
        confirm = self.ui.confirm.text()
        data = self.showdata(self.id)
        if data[0] == origin:
            if confirm == new:
                self.update_password(confirm)
                self.message = 'Reset successful!'
            else:
                self.message = 'Check your password!'

        else:
            self.message = 'Please check your password'

        show_box("Reset password", self.message)
        self.ui.pre_password.clear()
        self.ui.password.clear()
        self.ui.confirm.clear()

    def showdata(self, id):
        conn = sqlite3.connect(database)
        data = conn.execute("select PASSWORD from USER where ID='%s'" % id).fetchone()
        conn.close()
        return data

    def update_password(self, password):
        id = 'admin'
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute("update USER set PASSWORD='%s' where ID='%s'" % (password, id))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 调用暗黑主题的库
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # 创建登录界面并且显示
    main = Login()
    main.show()
    sys.exit(app.exec_())
