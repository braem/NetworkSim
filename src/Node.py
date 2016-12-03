from Segments.EthernetFrame import EthernetFrame
from Segments.IPDatagram import IPDatagram
from Segments.Segment import *
import Network

class Node:
    node_id = 0

    def __init__(self):

        self.node_id = Node.node_id
        Node.node_id += 1
        #stores {final destination, mininmun distance, next hop}
        #self.routing_table = {{}}

    '''returns the packets who's current location is this node'''
    def get_packets(self):
        global network

        my_packets = []
        for packet in network.packets:
            if packet.current_node == self.node_id:
                my_packets.append(packet)
        return my_packets






class Switch (Node):
    def __init__(self):
        Node.__init__(self)
        self.routing_table = {}

    def get_ethernet_header(self, message):
        return message.frame_header

    def get_ethernet_datagram(self, message):
        return message.ip_datagram

    def wrap_new_ethernet_frame(self, message, destination_id):
        #TODO the length of the header shouldn't be zero?
        return EthernetFrame(Header(self.node_id, destination_id, 0), message)

    def next_hop(self, dest_id):
        return Network.network.nodes[self.routing_table[dest_id]]


class Router (Switch):
    def __init__(self):
        Switch.__init__(self)

    def get_ip_header(self, message):
        return message.ip_header

    def get_ip_segment(self, message):
        return message.segment


    def wrap_new_ip_frame(self, message, source_id, destination_id):
        #TODO the length of the header shouldn't be zero?
        return IPDatagram(Header(source_id, destination_id, 0),message)


class Host (Router):
    def __init__(self):
        Router.__init__(self)

    def get_protocol_header(self, message):
        return message.header

    def get_protocol_message(self, message):
        return message.message

    def wrap_new_protocol_header(self, header, message):
        if isinstance(header, TCPHeader):
            return TCPSegment(header, message)
        elif isinstance(header, UDPHeader):
            return UDPSegment(header, message)
        else:
            return Segment(header, message)

    def send_message(self, dest_id, message_string):
        Network.network.create_messageTCP(self.node_id, dest_id, message_string)


