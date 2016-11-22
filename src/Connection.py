import string, time, math, random


"""Connection.py object for connection """
__author__ = "Darren Hendrickson"
__version__ = "1.0.0"


class Connection:

    counter = 0

    def __init__(self, sourceNode, destinationNode):
        Connection.counter += 1
        self.__connection_id = self.uniqid()                          # instance variable unique to each instance
        self.__connectionType = ""                                    # "Coax", "Fibre", or "Custom"
        self.__connectionSourceNode = sourceNode                      # the source node
        self.__connectionDestinationNode = destinationNode            # the source node
        self.__connectionLength = 0                                   # length of connection
        self.__connectionBandWidth = 0                                #bandwidth of connection - can set if custom connectionType

    def __del__(self):
        Connection.counter -= 1

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

    def getUniqueID(self):
        return self.__connection_id
