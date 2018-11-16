'''
Appstate Robotics
@author Dillon Carns
@author Eli McGalliard
@author Jason Kennedy
@author Nick Burkett
'''
from MainWindow import *
from PyQt5.QtWidgets import QApplication
import sys

def main():
    #TODO: Do everyting ui related.
    #print("Appstate Robotics")
    _main_window = QApplication(sys.argv)
    execute = MainWindow()
    sys.exit(_main_window.exec())


if __name__ == "__main__":
    main();