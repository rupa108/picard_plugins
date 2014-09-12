# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swapscript_dialog.ui'
#
# Created: Fri Sep 12 15:41:48 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SwapTagsDialog(object):
    def setupUi(self, SwapTagsDialog):
        SwapTagsDialog.setObjectName(_fromUtf8("SwapTagsDialog"))
        SwapTagsDialog.resize(400, 300)
        self.script_edit = QtGui.QTextEdit(SwapTagsDialog)
        self.script_edit.setGeometry(QtCore.QRect(10, 40, 381, 231))
        self.script_edit.setObjectName(_fromUtf8("script_edit"))
        self.runButton = QtGui.QPushButton(SwapTagsDialog)
        self.runButton.setGeometry(QtCore.QRect(320, 270, 71, 32))
        self.runButton.setCheckable(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.info = QtGui.QLabel(SwapTagsDialog)
        self.info.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))

        self.retranslateUi(SwapTagsDialog)
        QtCore.QMetaObject.connectSlotsByName(SwapTagsDialog)

    def retranslateUi(self, SwapTagsDialog):
        SwapTagsDialog.setWindowTitle(_translate("SwapTagsDialog", "Swap Tags Script", None))
        self.runButton.setText(_translate("SwapTagsDialog", "Run", None))

