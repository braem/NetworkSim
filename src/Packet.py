"""Defines the Packet class"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

class Packet:

    """This class is intended to wrap Ryan's Segment/Datagram/Frame for convenience in advancing the simulation."""

    '''Why is this here?

    Sprint 1: Right now, I need to keep track of:
        - what node the packet is at/is moving away from.
        - a packet-specific timer for connection delay.
    It makes no sense to store this information in the Network class.

    Sprint 2: Later on I'll also need to know if the packet is transmitting or propagating
    so I can tell what to do with it when the timer is up.
    '''

    def __init__(self, node):
        self.current_node = node

    def set_connection(self,connection):
        self.connection = connection