"""Connection.py object for connection """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class Connection:

    def __init__(self, sourceNode, destinationNode):
        self.id = self.assignID                                     # instance variable unique to each instance
        self.connectionType = ""                                    # "Coax", "Fibre", or "Custom"
        self.connectionNodes = [sourceNode, destinationNode]        # a pair of nodes
        self.connectionLength = 0                                   # length of connection
        self.connectionBandWidth = 0                                #bandwidth of connection - can set if custom connectionType

    def setConnectionType(self, cType):
        self.connectionType = cType

    def getConnectionType(self):
        return self.connectionType

#    def setConnectionNodes(self, source, dest):
#        self.connectionNodes = [source, dest]

    def getConnectionNodes(self):
        return self.connectionNodes

    def setConnectionLength(self, cLength):
        self.setConnectionLength(cLength)

    def getConnectionLength(self):
        return self.connectionLength

    def setConnectionBandwidth(self, cBandwidth):
        self.connectionBandWidth = cBandwidth

    def getConnectionBandwidth(self):
        return self.connectionBandWidth

    def createConnection(self, sourceNode, destNode):
        # draw connection based on location of supplied nodes
        print "create connection"
    def assignID(self):
        # code to assign unique id
        print "assign id"