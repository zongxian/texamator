# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quitter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(274, 91)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/TeXamator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Quit", None))
        self.label.setText(_translate("Dialog", "Do you really want to quit TeXamator ?", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_ok.setText(_translate("Dialog", "Ok", None))

import icones_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

