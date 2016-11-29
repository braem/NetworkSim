from MacroGUIForm import Ui_MainWindow
from PyQt4 import QtCore, QtGui

"""MacroGUI.py - main file for MacroGUI """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class MacroGUI:

     if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())