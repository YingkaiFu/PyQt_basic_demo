# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(110, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.time.setFont(font)
        self.time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.set_ip = QtWidgets.QPushButton(self.centralwidget)
        self.set_ip.setGeometry(QtCore.QRect(420, 60, 201, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_ip.sizePolicy().hasHeightForWidth())
        self.set_ip.setSizePolicy(sizePolicy)
        self.set_ip.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.set_ip.setObjectName("set_ip")
        self.file_2 = QtWidgets.QPushButton(self.centralwidget)
        self.file_2.setGeometry(QtCore.QRect(90, 420, 201, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_2.sizePolicy().hasHeightForWidth())
        self.file_2.setSizePolicy(sizePolicy)
        self.file_2.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.file_2.setObjectName("file_2")
        self.dialog = QtWidgets.QPushButton(self.centralwidget)
        self.dialog.setGeometry(QtCore.QRect(90, 60, 201, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog.sizePolicy().hasHeightForWidth())
        self.dialog.setSizePolicy(sizePolicy)
        self.dialog.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.dialog.setObjectName("dialog")
        self.video = QtWidgets.QPushButton(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(90, 240, 201, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        self.video.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.video.setObjectName("video")
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(422, 238, 191, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy)
        self.file.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.file.setObjectName("file")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 180, 63, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ip = QtWidgets.QLabel(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(506, 180, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ip.setFont(font)
        self.ip.setText("")
        self.ip.setObjectName("ip")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dialog, self.video)
        MainWindow.setTabOrder(self.video, self.file)
        MainWindow.setTabOrder(self.file, self.set_ip)
        MainWindow.setTabOrder(self.set_ip, self.file_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt Demo"))
        self.time.setText(_translate("MainWindow", "00:00:00"))
        self.set_ip.setText(_translate("MainWindow", "Text interaction"))
        self.file_2.setText(_translate("MainWindow", "File manager"))
        self.dialog.setText(_translate("MainWindow", "Dialog"))
        self.video.setText(_translate("MainWindow", "Screen recorder"))
        self.file.setText(_translate("MainWindow", "Open directory"))
        self.label_3.setText(_translate("MainWindow", "IP:"))
