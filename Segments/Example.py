from Segment import TCPSegment
from Segment import UDPSegment
from Header import TCPHeader
from Header import UDPHeader
from IPDatagram import IPDatagram
from EthernetFrame import EthernetFrame

"""Example.py: Example on how to use some of the segment features"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"

# ======================
# One stage at a time
# ===================
# Create a segment
segment = UDPSegment(UDPHeader(80, 80, 7777), "Hello World")
print segment

# Create an IP Datagram
datagram = IPDatagram("relevant data", segment)
print datagram

# Create an Ethernet Frame
eframe = EthernetFrame("relevant info", datagram)
print eframe

# ============================
# OR doing everything at once
# ========================
print "------------"
all = EthernetFrame("relevant info", IPDatagram("relevant data", UDPSegment(UDPHeader(80, 80, 7777), "Hello World")))
print all

# ===========================
# UDP Checksum example
# ======================
print "------------"
# print checksum result to test msg integrity
print segment.header.checkChecksum()  # suceeds packet integrity is fine

# damage UDP packet header
segment.header.src_port = 77
# print new checksum result
print segment.header.checkChecksum()  # fails packet integrity was damaged
