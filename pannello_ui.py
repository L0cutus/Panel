# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pannello.ui'
#
# Created: Sun Jun 28 22:44:18 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(219, 236)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtGui.QFrame.Panel)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(18, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(49, 56, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 3, 1)
        self.clientiPushButton = QtGui.QPushButton(Dialog)
        self.clientiPushButton.setObjectName("clientiPushButton")
        self.gridLayout.addWidget(self.clientiPushButton, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(49, 56, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 3, 1)
        self.ddtPushButton = QtGui.QPushButton(Dialog)
        self.ddtPushButton.setObjectName("ddtPushButton")
        self.gridLayout.addWidget(self.ddtPushButton, 3, 1, 1, 1)
        self.fattPushButton = QtGui.QPushButton(Dialog)
        self.fattPushButton.setObjectName("fattPushButton")
        self.gridLayout.addWidget(self.fattPushButton, 4, 1, 1, 1)
        self.magaPushButton = QtGui.QPushButton(Dialog)
        self.magaPushButton.setObjectName("magaPushButton")
        self.gridLayout.addWidget(self.magaPushButton, 5, 1, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 3)
        self.exitPushButton = QtGui.QPushButton(Dialog)
        self.exitPushButton.setObjectName("exitPushButton")
        self.gridLayout.addWidget(self.exitPushButton, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Pannello", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bitstream Vera Sans\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gestionale</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by TIME di S.Zamprogno</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clientiPushButton.setText(QtGui.QApplication.translate("Dialog", "Clienti", None, QtGui.QApplication.UnicodeUTF8))
        self.ddtPushButton.setText(QtGui.QApplication.translate("Dialog", "DDT", None, QtGui.QApplication.UnicodeUTF8))
        self.fattPushButton.setText(QtGui.QApplication.translate("Dialog", "Fatture", None, QtGui.QApplication.UnicodeUTF8))
        self.magaPushButton.setText(QtGui.QApplication.translate("Dialog", "Magazzino", None, QtGui.QApplication.UnicodeUTF8))
        self.exitPushButton.setText(QtGui.QApplication.translate("Dialog", "Esci", None, QtGui.QApplication.UnicodeUTF8))

