import sys
from SendMessageWindow import SendMessage_Window
from PyQt4 import QtGui


class SendMessageInterface(object):

    @staticmethod
    def openSendMessageWindow(protocol_list):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = SendMessage_Window(MainWindow)
        sys.exit(app.exec_())
