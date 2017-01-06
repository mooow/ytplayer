import sys
import PyQt5.uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from gengui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
    def search(self):
        print("Searching")

app = QApplication(sys.argv)
win = MainWindow()
ui = Ui_MainWindow()
ui.setupUi(win)

win.show()
app.exec_()
