from ui import UI
import sys
import PyQt5.uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QStringListModel
from gengui import Ui_MainWindow
import ytlib

class GUI(UI):
    def __init__(self):
        UI.__init__(self, self.on_next_song)
        self.app = QApplication(sys.argv)
        self.win = MainWindow(self)
    
    def main(self):
        UI.main(self)
        self.win.show()
        self.app.exec_()
        self.close()
    
    def on_next_song(self, res): self.win.next(res)


class MainWindow(QMainWindow, Ui_MainWindow):    
    def __init__(self, ui):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ui = ui
        self.list_model = QStringListModel()
        self.queue = []
        self.listViewQueue.setModel(self.list_model)
    
    def search(self):
        res = self.ui.download(self.lineEditSearchString.text())
        self.lineEditSearchString.clear()
        self.queue.append(ytlib.tostring(res))
        self.update()
    
    def next(self, res):
        self.queue.pop(0)
        self.update()
        self.statusBar.showMessage(ytlib.tostring(res))
    
    def update(self):
        self.list_model.setStringList(self.queue)
