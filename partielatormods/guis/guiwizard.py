# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard.ui'
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
        Dialog.resize(735, 983)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/TeXamator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame1 = QtGui.QFrame(Dialog)
        self.frame1.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(130, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(self.frame1)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/wizard.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_warning = QtGui.QLabel(self.frame1)
        self.label_warning.setWordWrap(True)
        self.label_warning.setObjectName(_fromUtf8("label_warning"))
        self.verticalLayout_2.addWidget(self.label_warning)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtGui.QLabel(self.frame1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.frame1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_browse = QtGui.QPushButton(self.frame1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_browse.setIcon(icon1)
        self.pushButton_browse.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.horizontalLayout.addWidget(self.pushButton_browse)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_3.addWidget(self.frame1, 0, 0, 1, 1)
        self.frame2 = QtGui.QFrame(Dialog)
        self.frame2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName(_fromUtf8("frame2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_tags = QtGui.QLabel(self.frame2)
        self.label_tags.setWordWrap(True)
        self.label_tags.setObjectName(_fromUtf8("label_tags"))
        self.gridLayout_4.addWidget(self.label_tags, 0, 0, 1, 1)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.label_5 = QtGui.QLabel(self.frame2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self._2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_tag1 = QtGui.QLineEdit(self.frame2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag1.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag1.setSizePolicy(sizePolicy)
        self.lineEdit_tag1.setObjectName(_fromUtf8("lineEdit_tag1"))
        self._2.addWidget(self.lineEdit_tag1, 1, 0, 1, 1)
        self.lineEdit_tag2 = QtGui.QLineEdit(self.frame2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag2.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag2.setSizePolicy(sizePolicy)
        self.lineEdit_tag2.setObjectName(_fromUtf8("lineEdit_tag2"))
        self._2.addWidget(self.lineEdit_tag2, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self._2.addWidget(self.label_6, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self._2, 1, 0, 1, 1)
        self._3 = QtGui.QHBoxLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.listWidget = QtGui.QListWidget(self.frame2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self._3.addWidget(self.listWidget)
        self._4 = QtGui.QVBoxLayout()
        self._4.setObjectName(_fromUtf8("_4"))
        self.pushButton_add = QtGui.QPushButton(self.frame2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/edit_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self._4.addWidget(self.pushButton_add)
        self.pushButton_remove = QtGui.QPushButton(self.frame2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/edit_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon3)
        self.pushButton_remove.setObjectName(_fromUtf8("pushButton_remove"))
        self._4.addWidget(self.pushButton_remove)
        spacerItem5 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self._4.addItem(spacerItem5)
        self._3.addLayout(self._4)
        self.gridLayout_4.addLayout(self._3, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame2, 1, 0, 1, 1)
        self.frame3 = QtGui.QFrame(Dialog)
        self.frame3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setObjectName(_fromUtf8("frame3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_header = QtGui.QLabel(self.frame3)
        self.label_header.setWordWrap(True)
        self.label_header.setObjectName(_fromUtf8("label_header"))
        self.gridLayout_2.addWidget(self.label_header, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.frame3)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 1)
        self.label_warning_2 = QtGui.QLabel(self.frame3)
        self.label_warning_2.setWordWrap(True)
        self.label_warning_2.setObjectName(_fromUtf8("label_warning_2"))
        self.gridLayout_2.addWidget(self.label_warning_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame3, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_back = QtGui.QPushButton(Dialog)
        self.pushButton_back.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon4)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.gridLayout.addWidget(self.pushButton_back, 1, 2, 1, 1)
        self.pushButton_next = QtGui.QPushButton(Dialog)
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next.setIcon(icon5)
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))
        self.gridLayout.addWidget(self.pushButton_next, 1, 3, 1, 1)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon6)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 0, 1, 1)
        self.pushButton_apply = QtGui.QPushButton(Dialog)
        self.pushButton_apply.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apply.setIcon(icon7)
        self.pushButton_apply.setObjectName(_fromUtf8("pushButton_apply"))
        self.gridLayout.addWidget(self.pushButton_apply, 1, 4, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton_apply, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Wizard", None))
        self.label_warning.setText(_translate("Dialog", "Warning ! This wizard will erase some of your settings !", None))
        self.label_3.setText(_translate("Dialog", "TeXamator needs to know a few things before it can fully work :\n"
"- how do you declare your exercises in your tex files ?\n"
"- what header do you use to compile your files (what comes before begin{document}) ?\n"
"\n"
"If you want, TeXamator can try to find out automatically. Just enter the location of one of your typical tex files with some exercices in it and hit the \"Next\" button.", None))
        self.pushButton_browse.setText(_translate("Dialog", "Browse", None))
        self.label_tags.setText(_translate("Dialog", "Here are the tags TeXamator found. You can add or delete tags from the list.", None))
        self.label_5.setText(_translate("Dialog", "What comes before an exercise ?", None))
        self.label_6.setText(_translate("Dialog", "What comes after ?", None))
        self.label_header.setText(_translate("Dialog", "Here is the header TeXamator is going to use each time it needs to compile a file.", None))
        self.label_warning_2.setText(_translate("Dialog", "Note that \\begin{document} must not appear here !", None))
        self.pushButton_back.setText(_translate("Dialog", "Back", None))
        self.pushButton_next.setText(_translate("Dialog", "Next", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_apply.setText(_translate("Dialog", "Apply", None))

import icones_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

