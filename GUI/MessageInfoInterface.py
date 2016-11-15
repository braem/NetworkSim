import sys
from MessageInfoWindow import MessageInfo_Window
from PyQt4 import QtGui


class MessageInfoInterface(object):

    @staticmethod
    def openMessageInfoWindow(protocol_list):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = MessageInfo_Window(MainWindow, protocol_list)
        sys.exit(app.exec_())
