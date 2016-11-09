from Segment import Segment
from Header import TCPHeader

"""TCPSegment.py: TCPSegment class that has both the message and the TCP header, extending from Segment"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


class TCPSegment(Segment):
    def __init__(self, segment_header, msg):
        assert isinstance(segment_header, TCPHeader), "ERROR: %s IS NOT A TCP HEADER" % (segment_header)
        Segment.__init__(self, segment_header, msg)
