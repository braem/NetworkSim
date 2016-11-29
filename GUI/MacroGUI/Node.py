import string, time, math, random


"""Node.py - node object """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class Node(object):

    counter = 0

    def __init__(self, nodeType, x, y):
        Node.counter += 1
        self.__Node_ID = self.uniqid()           # instance variable unique to each instance
        self.__NodeType = nodeType          # node type "PC", "Router", or "Switch"
        self.__X = x                        # position x value
        self.__Y = y                        # position y value
        self.__NetworkInfo = object         # object that holds addressing info etc
        self.isSelected = False

    def __del__(self):
        Node.counter -= 1

    # borrowed from http://gurukhalsa.me/2011/uniqid-in-python/
    def uniqid(more_entropy=False):
        m = time.time()
        uniqid = '%8x%05x' % (math.floor(m), (m - math.floor(m)) * 1000000)
        if more_entropy:
            valid_chars = list(set(string.hexdigits.lower()))
            entropy_string = ''
            for i in range(0, 10, 1):
                entropy_string += random.choice(valid_chars)
            uniqid = uniqid + entropy_string
        return uniqid

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

    def getUniqueID(self):
        return self.__Node_ID

    def toggleIsSelected(self):
        self.isSelected = not self.isSelected