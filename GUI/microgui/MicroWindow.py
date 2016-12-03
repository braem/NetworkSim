# Micro view GUI for CPSC 444 project
#
# Author: Lukas Pihl

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MessageInfoWindow import MessageInfo_Window

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Values():
    buttonHeight = 51
    buttonWidth = 121
    labelHeight = 31
    graphicWidth = 110
    windHeight = 400
    windWidth = 900


class MicroMainWindow(QMainWindow):

    def __init__(self):
        super(MicroMainWindow, self).__init__()

        self.conList = []
        self.deviceList = []
        self.lineList = []
        self.central_widget = None
        self.list_size = 0
        self.setObjectName(_fromUtf8("MainWindow"))
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))

        self.btnProgress = QPushButton(self.central_widget)

        self.forward = True
        self.stepCount = 0

        self.setup()

    def setup(self):
        # get list of devices
        temp_device_list = [1, 2, 3, 1]
        self.list_size = 4

        # Setup window
        self.resize(Values.windWidth, Values.windHeight)
        self.btnProgress.setGeometry(QRect(0, 0, 100, 30))
        self.btnProgress.setObjectName(_fromUtf8("btnProgress"))
        self.btnProgress.clicked.connect(self.clickedButton_Progress)

        # Setup Window
        total_width = (4 + MicroGraphicsLabel.myWidth) * (self.list_size - 1)
        for i in range(0, self.list_size):
            total_width += MicroHostFrame.myWidth

        # Setup device frames
        for i in range(0, self.list_size):
            temp_offset = 0
            for j in range(i, self.list_size):
                temp_offset += MicroHostFrame.myWidth
                if j != self.list_size - 1:
                    temp_offset += MicroGraphicsLabel.myWidth + 2
            pos_x = Values.windWidth / 2 + total_width / 2 - temp_offset
            pos_y = Values.windHeight / 2 - MicroHostFrame.myHeight / 2 + (MicroHostFrame.myHeight -
                                                                           self.getDeviceHeight(
                                                                               temp_device_list[i]))
            self.deviceList.append(self.makeDevicePanel(temp_device_list[i], pos_x, pos_y))

        # Setup graphic labels
        for i in range(0, self.list_size - 1):
            temp_offset = 0
            for j in range(i, self.list_size - 1):
                temp_offset += MicroHostFrame.getWidth() + MicroGraphicsLabel.getWidth() + 2
                pos_x = Values.windWidth / 2 + total_width / 2 - temp_offset
                pos_y = Values.windHeight / 2 - MicroHostFrame.myHeight / 2 + (MicroHostFrame.myHeight -
                                                                               MicroGraphicsLabel.getHeight())
            self.lineList.append(self.makeLine(temp_device_list[i], temp_device_list[i + 1], pos_x, pos_y))

        # Show components
        for i in self.deviceList:
            i.show()
        for i in self.lineList:
            i.show()
        self.setCentralWidget(self.central_widget)
        self.retranslateUi(self)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("MainWindow", "Micro View", None))
        if self.isvalid():
            for i in self.deviceList:
                i.retranslateUi()

    def isvalid(self):
        return True

    def getDeviceHeight(self, device):
        if device == 1:
            return MicroHostFrame.myHeight
        elif device == 2:
            return MicroRouterFrame.myHeight
        elif device == 3:
            return MicroSwitchFrame.myHeight
        return 0

    def makeDevicePanel(self, device, pos_x, pos_y):
        if device == 1:
            frame = MicroHostFrame(self.central_widget, pos_x, pos_y)
            return frame
        elif device == 2:
            frame = MicroRouterFrame(self.central_widget, pos_x, pos_y)
            return frame
        elif device == 3:
            frame = MicroSwitchFrame(self.central_widget, pos_x, pos_y)
            return frame

    def makeLine(self, device1, device2, pos_x, pos_y):
        label = MicroGraphicsLabel(self.central_widget, device1, device2, pos_x, pos_y)
        return label

    def updateState(self):
        for gfx in self.lineList:
            gfx.update()
        for div in self.deviceList:
            div.updateState()

    def increment(self):
        if self.forward:
            self.stepCount += 1
        else:
            self.stepCount -= 1

        if self.stepCount == 0:
            MessageInfo_Window.nextMessage()
            self.forward = True
            self.lineList[0].updateState(0)
            self.deviceList[0].updateState(0)
            # disable
            # setup next message
        elif self.stepCount == 1:
            self.lineList[0].updateState(1)
            self.deviceList[0].updateState(1)
            # enable App button and line segment of host1
        elif self.stepCount == 2:
            self.lineList[0].updateState(2)
            self.deviceList[0].updateState(2)
            # go to Trans button and line segment of host1
        elif self.stepCount == 3:
            self.lineList[0].updateState(3)
            self.deviceList[0].updateState(3)
            # go to Net button and line segment of host1
        elif self.stepCount == 4:
            self.lineList[0].updateState(4)
            self.deviceList[0].updateState(4)
            # go to Link button and line segment of host1
        elif self.stepCount == 5:
            self.lineList[0].updateState(5)
            self.deviceList[0].updateState(5)
            self.deviceList[1].updateState(0)
            # go to Phys button and line segment of host1
        elif self.stepCount == 6:
            self.lineList[0].updateState(6)
            self.deviceList[0].updateState(0)
            self.deviceList[1].updateState(3)
            # go to Phys button and line segment of router
        elif self.stepCount == 7:
            self.lineList[0].updateState(7)
            self.deviceList[1].updateState(2)
            # go to Link button and line segment of router
        elif self.stepCount == 8:
            self.lineList[0].updateState(8)
            self.lineList[1].updateState(0)
            self.deviceList[1].updateState(1)
            # go to Net button and line segment of router
        elif self.stepCount == 9:
            self.lineList[0].updateState(0)
            self.lineList[1].updateState(1)
            # change sides
        elif self.stepCount == 10:
            self.lineList[1].updateState(2)
            self.deviceList[1].updateState(2)
            # go to router Link button and line segment
        elif self.stepCount == 11:
            self.lineList[1].updateState(3)
            self.deviceList[1].updateState(3)
            self.deviceList[2].updateState(0)
            # go to router Phys button and line segment
        elif self.stepCount == 12:
            self.lineList[1].updateState(4)
            self.deviceList[1].updateState(0)
            self.deviceList[2].updateState(2)
            # go to switch Phys button and line segment
        elif self.stepCount == 13:
            self.lineList[1].updateState(5)
            self.lineList[2].updateState(0)
            self.deviceList[2].updateState(1)
            # go to switch Link button and line segment
        elif self.stepCount == 14:
            self.lineList[1].updateState(0)
            self.lineList[2].updateState(1)
            # change sides
        elif self.stepCount == 15:
            self.lineList[2].updateState(2)
            self.deviceList[2].updateState(2)
            self.deviceList[3].updateState(0)
            # go to switch Phys button and line segment
        elif self.stepCount == 16:
            self.lineList[2].updateState(3)
            self.deviceList[2].updateState(0)
            self.deviceList[3].updateState(5)
            # go to host2 Phys button and line segment
        elif self.stepCount == 17:
            self.lineList[2].updateState(4)
            self.deviceList[3].updateState(4)
            # go to host2 Link button and line segment
        elif self.stepCount == 18:
            self.lineList[2].updateState(5)
            self.deviceList[3].updateState(3)
            # go to host2 Net button and line segment
        elif self.stepCount == 19:
            self.lineList[2].updateState(6)
            self.deviceList[3].updateState(2)
            # go to host2 Trans button and line segment
        elif self.stepCount == 20:
            self.lineList[2].updateState(7)
            self.deviceList[3].updateState(1)
            # go to host2 App button and line segment
        elif self.stepCount == 21:
            self.forward = False
            self.lineList[2].updateState(0)
            self.deviceList[3].updateState(0)
            MessageInfo_Window.nextMessage()
            # disable
            # setup nest message

    def clickedButton_Progress(self):
        self.increment()


class MicroHostFrame(QFrame):
    myHeight = Values.buttonHeight*5+Values.labelHeight-5
    myWidth = Values.buttonWidth

    def __init__(self, holder, pos_x, pos_y):
        super(MicroHostFrame, self).__init__(holder)

        self.myHolder = holder

        self.btnHostA = QPushButton(self)
        self.btnHostT = QPushButton(self)
        self.btnHostN = QPushButton(self)
        self.btnHostL = QPushButton(self)
        self.btnHostP = QPushButton(self)
        self.lblHost = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroHostFrame.myWidth, MicroHostFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameHost"))
        self.btnHostA.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnHostA.setObjectName(_fromUtf8("btnHostA"))
        self.btnHostA.clicked.connect(self.clickedButton_Application)
        self.btnHostT.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth,
                                        Values.buttonHeight))
        self.btnHostT.setObjectName(_fromUtf8("btnHostT"))
        self.btnHostT.clicked.connect(self.clickedButton_Transport)
        self.btnHostN.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth,
                                        Values.buttonHeight))
        self.btnHostN.setObjectName(_fromUtf8("btnHostN"))
        self.btnHostN.clicked.connect(self.clickedButton_Network)
        self.btnHostL.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*3-4, Values.buttonWidth,
                                        Values.buttonHeight))
        self.btnHostL.setObjectName(_fromUtf8("btnHostL"))
        self.btnHostL.clicked.connect(self.clickedButton_Link)
        self.btnHostP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*4-5, Values.buttonWidth,
                                        Values.buttonHeight))
        self.btnHostP.setObjectName(_fromUtf8("btnHostP"))
        self.btnHostP.clicked.connect(self.clickedButton_Physical)
        self.lblHost.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblHost.setAlignment(Qt.AlignCenter)
        self.lblHost.setObjectName(_fromUtf8("lblHost"))
        self.updateState(0)

    def retranslateUi(self):
        self.btnHostA.setText(_translate("HostFrame", "Application", None))
        self.btnHostT.setText(_translate("HostFrame", "Transport", None))
        self.btnHostN.setText(_translate("HostFrame", "Network", None))
        self.btnHostL.setText(_translate("HostFrame", "Link", None))
        self.btnHostP.setText(_translate("HostFrame", "Physical", None))
        self.lblHost.setText(_translate("HostFrame", "Host", None))

    @staticmethod
    def getHeight():
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

    def clickedButton_Application(self):
        ui = MessageInfo_Window(self.myHolder, "Application")
        ui.show()

    def clickedButton_Transport(self):
        ui = MessageInfo_Window(self.myHolder, "Transport")
        ui.show()

    def clickedButton_Network(self):
        ui = MessageInfo_Window(self.myHolder, "Network")
        ui.show()

    def clickedButton_Link(self):
        ui = MessageInfo_Window(self.myHolder, "Link")
        ui.show()

    def clickedButton_Physical(self):
        ui = MessageInfo_Window(self.myHolder, "Physical")
        ui.show()

    def updateState(self, point):
        self.btnHostA.setDisabled(True)
        self.btnHostT.setDisabled(True)
        self.btnHostN.setDisabled(True)
        self.btnHostL.setDisabled(True)
        self.btnHostP.setDisabled(True)
        if point == 1:
            self.btnHostA.setDisabled(False)
        elif point == 2:
            self.btnHostT.setDisabled(False)
        elif point == 3:
            self.btnHostN.setDisabled(False)
        elif point == 4:
            self.btnHostL.setDisabled(False)
        elif point == 5:
            self.btnHostP.setDisabled(False)



class MicroRouterFrame(QFrame):
    myHeight = Values.buttonHeight*3+Values.labelHeight-3
    myWidth = Values.buttonWidth

    def __init__(self, holder, pos_x, pos_y):
        super(MicroRouterFrame, self).__init__(holder)

        self.myHolder = holder
        self.btnRouterN = QPushButton(self)
        self.btnRouterL = QPushButton(self)
        self.btnRouterP = QPushButton(self)
        self.lblRouter = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroRouterFrame.myWidth, MicroRouterFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameRouter"))

        self.btnRouterN.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnRouterN.setObjectName(_fromUtf8("btnRouterN"))
        self.btnRouterN.clicked.connect(self.clickedButton_Network)
        self.btnRouterL.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth,
                                          Values.buttonHeight))
        self.btnRouterL.setObjectName(_fromUtf8("btnRouterL"))
        self.btnRouterL.clicked.connect(self.clickedButton_Link)
        self.btnRouterP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth,
                                          Values.buttonHeight))
        self.btnRouterP.setObjectName(_fromUtf8("btnRouterP"))
        self.btnRouterP.clicked.connect(self.clickedButton_Physical)
        self.lblRouter.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblRouter.setAlignment(Qt.AlignCenter)
        self.lblRouter.setObjectName(_fromUtf8("lblRouter"))
        self.updateState(0)

    def retranslateUi(self):
        self.btnRouterN.setText(_translate("RouterFrame", "Network", None))
        self.btnRouterL.setText(_translate("RouterFrame", "Link", None))
        self.btnRouterP.setText(_translate("RouterFrame", "Physical", None))
        self.lblRouter.setText(_translate("RouterFrame", "Router", None))

    @staticmethod
    def getHeight():
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

    def clickedButton_Network(self):
        ui = MessageInfo_Window(self.myHolder, "Network")
        ui.show()

    def clickedButton_Link(self):
        ui = MessageInfo_Window(self.myHolder, "Link")
        ui.show()

    def clickedButton_Physical(self):
        ui = MessageInfo_Window(self.myHolder, "Physical")
        ui.show()

    def updateState(self, point):
        self.btnRouterN.setDisabled(True)
        self.btnRouterL.setDisabled(True)
        self.btnRouterP.setDisabled(True)
        if point == 1:
            self.btnRouterN.setDisabled(False)
        elif point == 2:
            self.btnRouterL.setDisabled(False)
        elif point == 3:
            self.btnRouterP.setDisabled(False)

class MicroSwitchFrame(QFrame):
    myHeight = Values.buttonHeight*2+Values.labelHeight-2
    myWidth = Values.buttonWidth

    def __init__(self, holder, pos_x, pos_y):
        super(MicroSwitchFrame, self).__init__(holder)
        self.myHolder = holder
        self.btnSwitchL = QPushButton(self)
        self.btnSwitchP = QPushButton(self)
        self.lblSwitch = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroSwitchFrame.myWidth, MicroSwitchFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameSwitch"))
        self.btnSwitchL.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnSwitchL.setObjectName(_fromUtf8("btnSwitchL"))
        self.btnSwitchL.clicked.connect(self.clickedButton_Link)
        self.btnSwitchP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth,
                                          Values.buttonHeight))
        self.btnSwitchP.setObjectName(_fromUtf8("btnSwitchP"))
        self.btnSwitchP.clicked.connect(self.clickedButton_Physical)
        self.lblSwitch.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblSwitch.setAlignment(Qt.AlignCenter)
        self.lblSwitch.setObjectName(_fromUtf8("lblSwitch"))
        self.updateState(0)

    def retranslateUi(self):
        self.btnSwitchL.setText(_translate("SwitchFrame", "Link", None))
        self.btnSwitchP.setText(_translate("SwitchFrame", "Physical", None))
        self.lblSwitch.setText(_translate("SwitchFrame", "Switch", None))

    @staticmethod
    def getHeight():
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

    def clickedButton_Link(self):
        ui = MessageInfo_Window(self.myHolder, "Link")
        ui.show()

    def clickedButton_Physical(self):
        ui = MessageInfo_Window(self.myHolder, "Physical")
        ui.show()

    def updateState(self, point):
        self.btnSwitchL.setDisabled(True)
        self.btnSwitchP.setDisabled(True)
        if point == 1:
            self.btnSwitchL.setDisabled(False)
        elif point == 2:
            self.btnSwitchP.setDisabled(False)


class MicroGraphicsLabel(QLabel):
    myHeight = Values.buttonHeight*5-5
    myWidth = Values.graphicWidth

    def __init__(self, holder, node1, node2, pos_x, pos_y):
        super(MicroGraphicsLabel, self).__init__(holder)

        self.node1 = node1
        self.node2 = node2
        self.listSize = 0
        self.myType = 0
        self.myMaps = []

        self.setup(pos_x, pos_y)

    def setup(self, posX, posY):
        self.setGeometry(posX, posY, MicroGraphicsLabel.myWidth, MicroGraphicsLabel.myHeight)
        cwd = os.getcwd()
        cwd = cwd.replace("\\", "/")
        self.myType = self.getType(self.node1, self.node2)
        if self.myType == 11:
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
        elif self.myType == 12:
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR0.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR1.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR2.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR3.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR4.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR5.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR6.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR7.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HR8.png"))
        elif self.myType == 13:
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
        elif self.myType == 21:
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
        elif self.myType == 23:
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS0.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS1.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS2.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS3.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS4.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/RS5.png"))
        elif self.myType == 31:
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH0.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH1.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH2.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH3.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH4.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH5.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH6.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/SH7.png"))
        elif self.myType == 32:
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
            self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
        self.setPixmap((self.myMaps[0]))
        self.setAlignment(Qt.AlignBottom)
        self.myLabel = self

    def buildMap(self, path):
        self.listSize += 1
        this_map = QPixmap(path)
        return this_map

    @staticmethod
    def getHeight():
        return MicroGraphicsLabel.myHeight

    @staticmethod
    def getWidth():
        return MicroGraphicsLabel.myWidth

    def getType(self, node1, node2):
        if node1 == 1:
            if node2 == 1:
                return 11
            if node2 == 2:
                return 12
            if node2 == 3:
                return 13
        if node1 == 2:
            if node2 == 1:
                return 21
            if node2 == 3:
                return 23
        if node1 == 3:
            if node2 == 1:
                return 31
            if node2 == 2:
                return 32
        return False

    def updateState(self, point):
        if point < self.listSize:
            self.setPixmap(self.myMaps[point])
        else:
            self.setPixmap((self.myMaps[0]))


# For testing purposes
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MicroMainWindow()
    ui.show()
    sys.exit(app.exec_())



