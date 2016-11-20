from Connection import *
from Node import *

"""GUINetwork.py - Collection of nodes and their connections """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class GUINetwork:

    def __init__(self):
        self.Nodes = []
        self.Connections = []

    def addNode(self, node):
        self.Nodes.append(node)

    def addConnection(self, connection):
        self.Connections.append(connection)

    def removeNode(self, nodeID):
        # some remove code
        print "remove node"
    def removeConnection(self, connectionID):
        # some remove code
        print "remove connection"