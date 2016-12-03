"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"


from Node import *
from Connection import Connection
from SimulationLoop import start_simulation
from SimulationLoop import SimThread

import Network
from routing_table_algo import routing_tables

def test_step(network):
    """Step function for use in the simulation"""

    print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for packet in network.packets.values():
        print "packet #", packet.packet_id


        if packet.timer > 0:
            print "transmitting on connection", packet.connection.connection_id
            print "Time steps to completion: " + str(packet.timer)
            packet.decrement_timer()
        elif packet.timer == 0:
            packet.update_location()

            try:
                print "packet", packet.packet_id, "has been forwarded onto connection", packet.connection.connection_id,\
                    "latency:", packet.connection.latency, "."
            except(AttributeError):
                print"packet has not been forwarded"

            if(packet.get_destination() == packet.current_node.node_id):
                print packet.payload.IPDatagram.Segment.message
                del(network.packets[packet.packet_id])
                print "packet", packet.packet_id, "has arrived at node", packet.current_node.node_id, "and been deleted."
        else:
            print "packet", packet.packet_id, "has neg timer, so it's just starting."
            packet.update_location()

        print "packet is at node " + str(packet.current_node.node_id)

def add_n_host_line(n):
    network = Network.network
    start = len(network.nodes)
    stop = start + n
    for j in range(start,stop):
        previous = j - 1
        this = j
        network.add_node(Host())
        if previous >= start:
            previous_node = network.nodes[previous]
            this_node = network.nodes[this]
            network.add_connection(previous_node.node_id, this_node.node_id, Connection(previous_node, this_node, 2))

def build_network():
    #Can think of this network as shaped like a boxy number eight.
    network = Network.network
    add_n_host_line(5)
    add_n_host_line(5)
    first = network.nodes[0]
    sixth = network.nodes[5]
    network.add_connection(0, 5,Connection(first, sixth, 1))
    third = network.nodes[2]
    eighth = network.nodes[7]
    network.add_connection(2, 7, Connection(third, eighth, 2))
    fifth = network.nodes[4]
    tenth = network.nodes[9]
    network.add_connection(4, 9, Connection(fifth, tenth, 3))

def table_print(arg):
    network=Network.network
    graph = network.get_as_graph()
    print "Network Connectivity Table"
    for node in network.nodes.keys():
        print node, graph[node]

    print ""

    print "Packet Table"

    for packet in network.packets.values():

       conn_id = "NA"

       try:
           conn_id = packet.connection.connection_id
       except: pass

       print "Pkt #" + str(packet.packet_id) + ":",\
             "Loc",   packet.current_node.node_id,\
             "Src",   packet.get_source(),\
             "Dst",   packet.get_destination(),\
             "Conn",  conn_id,\
             "ETA",   packet.timer


def start_demo():
    #initialize global network variable
    Network.network_init()
    network = Network.network
    build_network()
    send_message(0, 7, "Message")
    # Create a global SimThread
    global simulation
    print "Starting simulation"
    simulation = start_simulation(network,table_print,1)
    simulation.join()#At this point, we want to go back to the UI code.
    print "Simulation all done now =)"

def stop_demo():
    simulation.end()

def get_routing_table(node_id):
    table = Network.network.nodes[node_id].routing_table
    print"Node #" + str(node_id)
    for node in table:
        print node, ": ", table[node]

def send_message(src_id, dest_id, msg):
    #Wrapped Network function for convenience.
    Network.network.create_messageUDP(src_id, dest_id, msg)

def add_node(connected_node_id, latency):
    #User may only add a node which is connected to another node
    network = Network.network
    connected_node = network.nodes[connected_node_id]
    new_node = Host()
    network.add_node(new_node)
    network.add_connection(new_node.node_id, connected_node_id, Connection(new_node, connected_node, latency))

def remove_node(node_id):
    #Wrapped Network function for convenience
    Network.network.remove_node(node_id)

def n_node_demo(n):
    """Creates a linear network of n Hosts, and sends a single Packet along the network."""
    #Already have a global network instance, but it's empty.
    #Now we need a few host nodes.
    network = Network.network
    add_n_host_line(n)

    tables = routing_tables(network)

    #Set the routing tables in all the nodes
    for node in network.nodes.values():
        node.routing_table=tables[node.node_id]

    #Create one message to start off
    network.create_messageUDP(0, n-1, "Message")

    # Create a SimThread that will run a little longer than the total connection and processing latency.
    simulation = SimThread(test_step, network)
    print "Starting simulation"
    simulation.start()
    simulation.join()
    print "Simulation all done now =)"

start_demo()


