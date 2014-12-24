# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linkDisplay.ui'
#
# Created: Wed Dec 17 13:15:28 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 80)
        Dialog.setMinimumSize(QtCore.QSize(360, 80))
        Dialog.setMaximumSize(QtCore.QSize(360, 80))
        self.okButton = QtGui.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(140, 50, 85, 27))
        self.okButton.setObjectName("okButton")
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 341, 31))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Link URL", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

