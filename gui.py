# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Dec 24 14:06:45 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.titleEdit = QtGui.QLineEdit(self.centralwidget)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 0, 1, 1, 1)
        self.extBox = QtGui.QComboBox(self.centralwidget)
        self.extBox.setObjectName("extBox")
        self.extBox.addItem("")
        self.extBox.addItem("")
        self.extBox.addItem("")
        self.extBox.addItem("")
        self.gridLayout.addWidget(self.extBox, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.descEdit = QtGui.QLineEdit(self.centralwidget)
        self.descEdit.setObjectName("descEdit")
        self.gridLayout.addWidget(self.descEdit, 0, 4, 1, 1)
        self.textEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName("menubar")
        self.menuGist = QtGui.QMenu(self.menubar)
        self.menuGist.setObjectName("menuGist")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload = QtGui.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDisplay_Last_URL = QtGui.QAction(MainWindow)
        self.actionDisplay_Last_URL.setObjectName("actionDisplay_Last_URL")
        self.menuGist.addAction(self.actionUpload)
        self.menuGist.addAction(self.actionDisplay_Last_URL)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGist.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gist Uploader", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.extBox.setItemText(0, QtGui.QApplication.translate("MainWindow", ".py", None, QtGui.QApplication.UnicodeUTF8))
        self.extBox.setItemText(1, QtGui.QApplication.translate("MainWindow", ".cpp", None, QtGui.QApplication.UnicodeUTF8))
        self.extBox.setItemText(2, QtGui.QApplication.translate("MainWindow", ".txt", None, QtGui.QApplication.UnicodeUTF8))
        self.extBox.setItemText(3, QtGui.QApplication.translate("MainWindow", ".c", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGist.setTitle(QtGui.QApplication.translate("MainWindow", "Gist", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpload.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplay_Last_URL.setText(QtGui.QApplication.translate("MainWindow", "Display Last URL", None, QtGui.QApplication.UnicodeUTF8))

