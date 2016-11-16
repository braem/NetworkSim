from Header import Header
from Header import TCPHeader
from Header import UDPHeader

"""Segment.py: For creating segments containing a header & message"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


class Segment:
    # Initializes segment variables
    def __init__(self, segment_header, msg):
        assert isinstance(segment_header, Header), "ERROR: %s IS NOT A (TCP/UDP)HEADER" % (segment_header)
        self.header = segment_header
        self.message = msg

    # default print notation when printing a Segment
    def __str__(self):
        return "[[SEGMENT HEADER: %s ], MESSAGE: %s]" % (self.header, self.message)


class TCPSegment(Segment):
    def __init__(self, segment_header, msg):
        assert isinstance(segment_header, TCPHeader), "ERROR: %s IS NOT A TCP HEADER" % (segment_header)
        Segment.__init__(self, segment_header, msg)


class UDPSegment(Segment):
    def __init__(self, segment_header, msg):
        assert isinstance(segment_header, UDPHeader), "ERROR: %s IS NOT A UDP HEADER" % (segment_header)
        Segment.__init__(self, segment_header, msg)