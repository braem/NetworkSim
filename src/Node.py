"""Node.py - node object """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class Node(object):

    counter = 0

    def __init__(self, node_id, nodeType, x, y):
        Node.counter += 1
        self.__Node__ID = node_id           # instance variable unique to each instance
        self.__NodeType = nodeType          # node type "PC", "Router", or "Switch"
        self.__X = x                        # position x value
        self.__Y = y                        # position y value
        self.__NetworkInfo = object         # object that holds addressing info etc

    def __del__(self):
        Node.counter -= 1

    def setType(self, nType):
        self.__NodeType = nType

    def getType(self):
        return self.__NodeType

    def setLocation(self, xPos, yPos):
        self.__X = xPos
        self.__Y = yPos

    def getLocation(self):
        return [self.__X, self.__Y]

    def setNetworkInfo(self, networkInfo):
        self.__NetworkInfo = networkInfo

    def getNetworkInfo(self):
        return self.__NetworkInfo
