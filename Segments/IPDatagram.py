from Segment import Segment

"""IPDatagram.py:  IPDatagram class that has both a Segment object and a IP header"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


class IPDatagram:
    def __init__(self, header, seg):
        assert isinstance(seg, Segment), "ERROR: %s IS NOT A (TCP/UDP)SEGMENT " % (seg)
        self.ip_header = header
        self.segment = seg

    # default print notation when printing an IPDatagram
    def __str__(self):
        return "[IP HEADER: %s , %s]" % (self.ip_header, self.segment)
