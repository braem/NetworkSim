from Segment import Segment
from Header import UDPHeader

"""UDPSegment.py: UDPSegment class that has both the message and the UDP header, extending from Segment"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


class UDPSegment(Segment):
    def __init__(self, segment_header, msg):
        assert isinstance(segment_header, UDPHeader), "ERROR: %s IS NOT A UDP HEADER" % (segment_header)
        Segment.__init__(self, segment_header, msg)
