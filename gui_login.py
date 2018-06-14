# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_login.ui'
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
        Dialog.resize(172, 150)
        Dialog.setMinimumSize(QtCore.QSize(172, 150))
        Dialog.setMaximumSize(QtCore.QSize(172, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/access-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.leditUsuario = QtGui.QLineEdit(Dialog)
        self.leditUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.leditUsuario.setObjectName(_fromUtf8("leditUsuario"))
        self.verticalLayout.addWidget(self.leditUsuario)
        self.leditPassword = QtGui.QLineEdit(Dialog)
        self.leditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.leditPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.leditPassword.setObjectName(_fromUtf8("leditPassword"))
        self.verticalLayout.addWidget(self.leditPassword)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSignIn = QtGui.QPushButton(Dialog)
        self.btnSignIn.setObjectName(_fromUtf8("btnSignIn"))
        self.horizontalLayout.addWidget(self.btnSignIn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Libra", None))
        self.label.setText(_translate("Dialog", "Libra", None))
        self.leditUsuario.setPlaceholderText(_translate("Dialog", "Usuario", None))
        self.leditPassword.setPlaceholderText(_translate("Dialog", "Contraseña", None))
        self.btnSignIn.setText(_translate("Dialog", "Sign In", None))

import res_rc
