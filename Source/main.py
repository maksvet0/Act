import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from actgui import Ui_Window

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("windows.png"))
        self.ui.ActBtn.clicked.connect(self.Activate)
    def Activate(self):
        arg = self.ui.ChangeVer.currentText()
        if arg == "Windows 10/11 Pro":
            os.system("slmgr /ipk M7XTQ-FN8P6-TTKYV-9D4CC-J462D")
            os.system("slmgr /skms kms.digiboy.ir")
            os.system("slmgr /ato")
        if arg == "Windows 10 LTSC/LTSB":
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            os.system("slmgr /skms kms.digiboy.ir")
            os.system("slmgr /ato")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Appl = App()
    Appl.show()
    sys.exit(app.exec())
