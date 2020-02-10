# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\download.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView


class Ui_File_Browser(object):
    def setupUi(self, File_Browser):
        File_Browser.setObjectName("File_Browser")
        File_Browser.resize(874, 564)
        self.centralwidget = QtWidgets.QWidget(File_Browser)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 571, 491))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(730, 480, 131, 25))
        self.state.setText("")
        self.state.setObjectName("state")
        self.rest = QtWidgets.QLabel(self.centralwidget)
        self.rest.setGeometry(QtCore.QRect(750, 30, 111, 25))
        self.rest.setText("")
        self.rest.setObjectName("rest")
        self.all = QtWidgets.QLabel(self.centralwidget)
        self.all.setGeometry(QtCore.QRect(750, 60, 111, 25))
        self.all.setText("")
        self.all.setObjectName("all")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(650, 90, 191, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fetch_data = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_data.sizePolicy().hasHeightForWidth())
        self.fetch_data.setSizePolicy(sizePolicy)
        self.fetch_data.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.fetch_data.setObjectName("fetch_data")
        self.verticalLayout.addWidget(self.fetch_data)
        self.delete_file = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_file.sizePolicy().hasHeightForWidth())
        self.delete_file.setSizePolicy(sizePolicy)
        self.delete_file.setStyleSheet("border: 1px solid black;\n"
"border-radius: 15px;\n"
"font-size: 25px;")
        self.delete_file.setObjectName("delete_file")
        self.verticalLayout.addWidget(self.delete_file)
        File_Browser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(File_Browser)
        self.statusbar.setObjectName("statusbar")
        File_Browser.setStatusBar(self.statusbar)

        self.retranslateUi(File_Browser)
        QtCore.QMetaObject.connectSlotsByName(File_Browser)

    def retranslateUi(self, File_Browser):
        _translate = QtCore.QCoreApplication.translate
        File_Browser.setWindowTitle(_translate("File_Browser", "File Browser"))
        self.fetch_data.setText(_translate("File_Browser", "Fetch data"))
        self.delete_file.setText(_translate("File_Browser", "Delete file"))
