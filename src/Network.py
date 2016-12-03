from Segments.Segment import *
from Segments.Header import *
from Segments.IPDatagram import IPDatagram
from Segments.EthernetFrame import EthernetFrame
from Packet import Packet
from Connection import Connection
import Node

class Network:
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.packets = {}

    def add_node(self, node):
        """
        add a node to the network
        """
        self.nodes[node.node_id] = node

    def get_node_pair_id(self, n1_id, n2_id):
        return (n1_id, n2_id) if n1_id <= n2_id else (n2_id, n1_id)

    def create_messageUDP(self, startID, endID, messageString):

        segment = UDPSegment(UDPHeader(startID, endID, 0), messageString)
        self.create_message(startID, endID, segment)


    def create_messageTCP(self, startID, endID, messageString):

        segment = TCPSegment(TCPHeader(startID, endID, 0), messageString)
        self.create_message(startID, endID, segment)


    def create_message(self, startID, endID, UDP_TCP_segment):
        ip_datagram = IPDatagram(Header(startID,endID,0), UDP_TCP_segment)
        eth_frame = EthernetFrame(Header(startID, endID, 0), ip_datagram)
        self.add_packet(Packet(self.nodes[startID], eth_frame))

        
    def add_connection(self, n1_id, n2_id, connection):
        """
        add a connection between two nodes (by id)
        """
        pair_id = self.get_node_pair_id(n1_id, n2_id)
        self.connections[pair_id] = connection

    def add_packet(self, packet):
        self.packets[packet.packet_id] = packet

    def remove_node(self, node_id):
        """
        remove a node by id
        """
        try:
            del self.nodes[node_id]
            for c_id in self.connections.keys():
                if node_id in c_id:
                    del self.connections[c_id]
            for p_id, packet in self.packets.iteritems():
                if node_id == packet.current_node.node_id:
                    del self.packets[p_id]
            # for node in self.nodes.values():
            #     if not self.get_connected_nodes(node): self.remove_node(node.node_id)
            return True
        except:
            return False



    def remove_connection(self, n1_id, n2_id):
        """
        remove a connection by ids of nodes
        """
        try:
            del self.connections[self.get_node_pair_id(n1_id, n2_id)]
            return True
        except:
            return False

    def get_connected_nodes(self, node_id):
        """
        returns a list of nodes connected to the given node in the form
        [{"node": the node at the other end, "connection": the connection object}]
        """
        connected = []
        for c_id, connection in self.connections.iteritems():
            if node_id in c_id:
                other_node = c_id[0] if c_id[1] == node_id else c_id[1]
                connected.append({"node":other_node, "connection":connection})
        return connected

    def get_as_graph(self):
        graph = {}
        for node in self.nodes:
            graph_node = {}
            for connection in self.get_connected_nodes(node):
                graph_node[connection["node"]] = connection["connection"].latency
            graph[node] = graph_node
        return graph

def network_init():
    global network
    network = Network()
    Node.Node.node_id=0
    Connection.static_id=0
    Packet.static_packet_id = 0
