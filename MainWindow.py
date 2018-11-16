'''
creates only the main window.
All attributes should be added onto this.
Basic example for creating a window using PyQt5.
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
