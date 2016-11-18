from EthernetFrame import EthernetFrame
from IPDatagram import IPDatagram
from Header import Header
from Header import TCPHeader
from Header import UDPHeader
from Segment import TCPSegment
from Segment import UDPSegment
from Segment import Segment

class Node:
    node_id = 0

    def __init__(self):
        self.node_id = self.Node.node_id
        self.Node.node_id += 1


class Switch (Node):
    def __init__(self):
        pass

    def get_ethernet_header(self, message):
        return message.frame_header

    def get_ethernet_datagram(self, message):
        return message.ip_datagram

    def wrap_new_ethernet_frame(self, message, destination_id):
        #TODO the length of the header shouldn't be zero?
        return EthernetFrame(Header(self.node_id, destination_id, 0), message)


class Router (Switch):
    def __init__(self):
        pass

    def get_ip_header(self, message):
        return message.ip_header

    def get_ip_segment(self, message):
        return message.segment


    def wrap_new_ip_frame(self, message, source_id, destination_id):
        #TODO the length of the header shouldn't be zero?
        return IPDatagram(Header(source_id, destination_id, 0),message)


class Host (Router):
    def __init__(self):
        pass

    def get_protocol_header(self, message):
        return message.header

    def get_protocol_message(self, message):
        return message.message

    def wrap_new_protocol_header(self, header, message):
        if isinstance(header, TCPHeader):
            TCPSegment(header, message)
        elif isinstance(header, UDPHeader):
            UDPSegment(header, message)
        else:
            Segment(header, message)