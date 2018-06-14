
import sys
import sqlite3

from PyQt4 import QtGui
from PyQt4 import QtCore

from gui_login import Ui_Dialog as LoginGui

import mec_login


class Login(QtGui.QDialog, LoginGui):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        ### functionality ###
        self.btnSignIn.clicked.connect(self.iniciar)

        ### database ###
        self.conn = sqlite3.connect(".libra.db")
        self.c = self.conn.cursor()
        mec_login.create_login_table(self.c, self.conn)
        self.show()

    def iniciar(self):

        usuario = self.leditUsuario.text()
        password = self.leditPassword.text()

        if mec_login.check_login(self.c, usuario, password):
            self.accept()

        else:
            self.leditUsuario.clear()
            self.leditPassword.clear()
            QtGui.QMessageBox.warning(self, 'Error', 'Incorrect username or password')


    def closeEvent(self, e):
        print("closing")
        self.c.close()
        self.conn.close()
        e.accept()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtGui.QDialog.Accepted:
        print('login successful')
    else:
        print('login unsuccessful')
    sys.exit(app.exec_())

