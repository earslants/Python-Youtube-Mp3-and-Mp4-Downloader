# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YoutubeConverter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 301)
        MainWindow.setWindowIcon(QIcon('yt.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_url.setGeometry(QtCore.QRect(380, 30, 61, 41))
        self.lbl_url.setObjectName("lbl_url")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setGeometry(QtCore.QRect(80, 80, 661, 22))
        self.txt_url.setObjectName("txt_url")
        self.btn_mp3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mp3.setGeometry(QtCore.QRect(260, 150, 93, 28))
        self.btn_mp3.setObjectName("btn_mp3")
        self.btn_mp4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mp4.setGeometry(QtCore.QRect(470, 150, 93, 28))
        self.btn_mp4.setObjectName("btn_mp4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Youtube Video Converter", "Youtube Video Converter"))
        self.lbl_url.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">URL</span></p></body></html>"))
        self.btn_mp3.setText(_translate("MainWindow", "MP3"))
        self.btn_mp4.setText(_translate("MainWindow", "MP4"))

