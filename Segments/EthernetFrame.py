from IPDatagram import IPDatagram

"""EthernetFrame.py: EthernetFrame class that has both a frame header and an IPDatagram """
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


class EthernetFrame:
    def __init__(self, header, datagram):
        assert isinstance(datagram, IPDatagram), "ERROR: %s IS NOT AN IPDATAGRAM " % (datagram)
        self.frame_header = header
        self.ip_datagram = datagram

    # default print notation when printing an Ethernet Frame
    def __str__(self):
        return "[FRAME HEADER: %s , %s]" % (self.frame_header, self.ip_datagram)
