"""Node.py - node object """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class Node:

    def __init__(self, node_id):
        self.id = node_id            # instance variable unique to each instance
        self.nodeType = ""      # node type "PC", "Router", or "Switch"
        self.x = 0              # position x value
        self.y = 0              # position y value
        self.image = ""         # path to image

    def setType(self, nType):
        self.nodeTypetype = nType

    def getType(self):
        return self.nodeType

    def setLocation(self, xPos, yPos):
        self.x = xPos
        self.y = yPos

    def getLocation(self):
        return [self.x, self.y]
