#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import os
import sys
import subprocess

from PyQt4.QtCore import PYQT_VERSION_STR, QDate, QFile
from PyQt4.QtCore import QRegExp, QString, QVariant, Qt
from PyQt4.QtCore import SIGNAL, QModelIndex, QSettings
from PyQt4.QtCore import QSize, QPoint

from PyQt4.QtGui  import QApplication, QCursor, QDateEdit
from PyQt4.QtGui  import QDialog, QMainWindow, QHBoxLayout
from PyQt4.QtGui  import QLabel, QLineEdit, QMessageBox, QPixmap
from PyQt4.QtGui  import QTabWidget, QPushButton, QRegExpValidator
from PyQt4.QtGui  import QStyleOptionViewItem, QTableView, QVBoxLayout
from PyQt4.QtGui  import QDataWidgetMapper, QTextDocument, QStyle
from PyQt4.QtGui  import QColor, QBrush, QTextOption
from PyQt4.QtGui  import QItemSelectionModel,QStandardItemModel
from PyQt4.QtGui  import QAbstractItemView, QIntValidator
from PyQt4.QtGui  import QDoubleValidator, QIcon, QFileDialog


import pannello_ui

__version__ = '0.2.0'

# usate per il salvataggio dei settings dell'applicazione
PNLORG = "TIME di Stefano Z."
PNLAPP = "Pannello Gestionale"
PNLDOMAIN = "zamprogno.it"

class PannelloDialog(QDialog, pannello_ui.Ui_Dialog):
    '''
    Pannello Gestionale v.0.2.0
    by TIME di Stefano Zamprogno
    @2009
    '''
    CLI, DDT, FATT, MAGA = range(4)

    def __init__(self, parent=None):
        super(PannelloDialog, self).__init__(parent)

        self.setupUi(self)
        self.restoreWinSettings()
        self.setupUiSignals()

    def setupUiSignals(self):
        self.connect(self.clientiPushButton, SIGNAL("clicked()"),
                    lambda: self.showFeat(PannelloDialog.CLI))
        self.connect(self.ddtPushButton, SIGNAL("clicked()"),
                    lambda: self.showFeat(PannelloDialog.DDT))
        self.connect(self.fattPushButton, SIGNAL("clicked()"),
                    lambda: self.showFeat(PannelloDialog.FATT))
        self.connect(self.magaPushButton, SIGNAL("clicked()"),
                    lambda: self.showFeat(PannelloDialog.MAGA))
        self.connect(self.exitPushButton, SIGNAL("clicked()"),
                    self.close)

    def closeEvent(self, event):
        settings = QSettings()
        settings.setValue("PannelloDialog/Geometry", QVariant(
                          self.saveGeometry()))

    def restoreWinSettings(self):
        settings = QSettings()
        self.restoreGeometry(
                settings.value("PannelloDialog/Geometry").toByteArray())

    def showFeat(self, act):
        if act == PannelloDialog.CLI:
            relpath = os.path.dirname(__file__)
            if relpath:
                relpath = "%s/" % relpath
            subprocess.Popen(['python',os.path.join("%s../clienti/" %
                                            relpath, "clienti.py")])
        elif act == PannelloDialog.FATT:
            relpath = os.path.dirname(__file__)
            if relpath:
                relpath = "%s/" % relpath
            subprocess.Popen(['python',os.path.join("%s../fatture/" %
                                            relpath, "fatture.py")])
        elif act == PannelloDialog.DDT:
            relpath = os.path.dirname(__file__)
            if relpath:
                relpath = "%s/" % relpath
            subprocess.Popen(['python',os.path.join("%s../ddt/" %
                                            relpath, "ddt.py")])
        elif act == PannelloDialog.MAGA:
            relpath = os.path.dirname(__file__)
            if relpath:
                relpath = "%s/" % relpath
            subprocess.Popen(['python',os.path.join("%s../magazzino/" %
                                            relpath, "magazzino.py")])


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName(PNLORG)
    app.setOrganizationDomain(PNLDOMAIN)
    app.setApplicationName(PNLAPP)

    form = PannelloDialog()
    form.show()
    app.exec_()
    del form

main()

