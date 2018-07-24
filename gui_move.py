# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_mover.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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
        Dialog.resize(313, 99)
        Dialog.setMinimumSize(QtCore.QSize(227, 99))
        Dialog.setMaximumSize(QtCore.QSize(500, 99))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/swap-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.spnboxQuantity = QtGui.QSpinBox(Dialog)
        self.spnboxQuantity.setMinimum(1)
        self.spnboxQuantity.setMaximum(99999)
        self.spnboxQuantity.setObjectName(_fromUtf8("spnboxQuantity"))
        self.horizontalLayout_2.addWidget(self.spnboxQuantity)
        self.leditCode = QtGui.QLineEdit(Dialog)
        self.leditCode.setReadOnly(True)
        self.leditCode.setObjectName(_fromUtf8("leditCode"))
        self.horizontalLayout_2.addWidget(self.leditCode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.leditFromGroup = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leditFromGroup.sizePolicy().hasHeightForWidth())
        self.leditFromGroup.setSizePolicy(sizePolicy)
        self.leditFromGroup.setReadOnly(True)
        self.leditFromGroup.setObjectName(_fromUtf8("leditFromGroup"))
        self.horizontalLayout.addWidget(self.leditFromGroup)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.cmboxToGroup = QtGui.QComboBox(Dialog)
        self.cmboxToGroup.setEditable(True)
        self.cmboxToGroup.setObjectName(_fromUtf8("cmboxToGroup"))
        self.horizontalLayout.addWidget(self.cmboxToGroup)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnConfirm = QtGui.QPushButton(Dialog)
        self.btnConfirm.setObjectName(_fromUtf8("btnConfirm"))
        self.horizontalLayout_3.addWidget(self.btnConfirm)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Move", None))
        self.label.setText(_translate("Dialog", "Move:", None))
        self.label_3.setText(_translate("Dialog", "From group:", None))
        self.label_4.setText(_translate("Dialog", "To group:", None))
        self.btnConfirm.setText(_translate("Dialog", "Confirm", None))

import res_rc
