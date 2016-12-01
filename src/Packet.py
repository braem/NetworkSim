"""Defines the Packet class"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

#import SimulationLoop

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
    #Need an id so the Packet dictionary in Network works the same as the others
    static_packet_id = 0
    def __init__(self, node, payload):
        self.connection = None
        self.payload = payload
        self.current_node = node
        self.packet_id = Packet.static_packet_id
        Packet.static_packet_id += 1

    def set_connection(self, connection):
        if self.connection is not None:
            self.connection.removeTraffic()
        self.connection = connection
        self.connection.addTraffic()
        self.set_timer(connection.latency)

    def set_timer(self, time):
        self.timer = time

    def decrement_timer(self):
        self.timer -= 1

    def update_location(self):
        global the_network

        if self.current_node != self.get_destination():
            # Updates what node the packet thinks it's at
            self.deliver()
            #get the next node and set this packet's connection to that between current_node and next_node
            next_node = self.current_node.next_hop(self.get_destination())
            self.set_connection(the_network.connections(self.current_node, next_node))
        else:
            #If the packet has reached its destination, delete it.
            self.connection.removeTraffic()
            del(the_network.packets[self.packet_id])

    def deliver(self):
        self.current_node = self.connection.other_node(self.current_node)
        del(self.connection)

    def get_destination(self):
        return self.payload.ip_datagram.segment.header.dest_port

