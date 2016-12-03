"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"


from Node import *
from Connection import Connection
from SimulationLoop import start_simulation
from SimulationLoop import SimThread
import time

import Network
from routing_table_algo import routing_tables

#step function template
# print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# for packet in network.packets.values():
#     if packet.timer > 0:
#         packet.decrement_timer()
#     elif packet.timer == 0:
#         packet.update_location()
#         if(packet.get_destination() == packet.current_node.node_id):
#             print packet.payload.ip_datagram.segment.message
#             del(network.packets[packet.packet_id])
#     else:
#         packet.update_location()
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
                conn_id = packet.connection.connection_id
            except(AttributeError):
                conn_id = -1

            if conn_id == -1:
                print "packet", packet.packet_id, "has not been forwarded"
            else:
                print "packet", packet.packet_id, "has been forwarded onto connection", packet.connection.connection_id,\
                    "latency:", str(packet.connection.latency) + "."


            if(packet.get_destination() == packet.current_node.node_id):

                del(network.packets[packet.packet_id])
                print "packet", packet.packet_id, "has arrived at node", packet.current_node.node_id, "and been deleted."
                print "It was carrying the message:"
                print packet.payload.ip_datagram.segment.message
        else:
            print "packet", packet.packet_id, "has neg timer, so it's just starting."
            packet.update_location()

        print "packet is at node " + str(packet.current_node.node_id)

def table_step(network):
    print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print get_packet_table()

    for packet in network.packets.values():
        if (packet.get_destination() == packet.current_node.node_id):
            print "Packet #" + str(packet.packet_id) + " delivered: " + packet.payload.ip_datagram.segment.message
        if packet.timer > 0:
            packet.decrement_timer()
        elif packet.timer == 0:
            packet.update_location()
        else:
            packet.update_location()

    time.sleep(1)



def get_graph():
    network = Network.network
    graph = network.get_as_graph()
    string = "Network Connectivity Table\n"
    for node in network.nodes.keys():
        string += str(node) + " " + str(graph[node]) + "\n"
    return string

def get_packet_table():
    string = "Packet Table\n"

    for packet in Network.network.packets.values():
        conn_id = "NA"
        next = "NA"
        try:
            conn_id = packet.connection.connection_id
            next = packet.connection.other_node(packet.current_node).node_id
        except: pass
        finally:

            #The +1 takes into account the implicit one-step processing time for each packet on arrival
            ETA = packet.timer + 1
            if packet.timer == -1:
                ETA = "NA"

            string += "Pkt #" + str(packet.packet_id) + ":" + \
                " Loc " + str(packet.current_node.node_id) + \
                " Nxt " + str(next) +\
                " Src " + str(packet.get_source()) + \
                " Dst " + str(packet.get_destination()) + \
                " Conn " + str(conn_id) + \
                " ETA " + str(ETA)
            string += "\n"
    return string



def get_table():
    return get_packet_table()

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


def start_demo():
    print"start_demo"
    #initialize global network variable
    Network.network_init()
    network = Network.network
    build_network()
    send_message(0,7,"First Message")
    # Create a global SimThread
    global simulation
    print "Starting simulation"
    simulation = start_simulation(network,table_step)
    #simulation.join()#At this point, we want to go back to the UI code, so we don't want this anymore.

def resume_demo():
    global simulation
    simulation=start_simulation(Network.network, table_step)

def stop_demo():
    simulation.end()

def get_routing_table(node_id):
    string =""

    table = Network.network.nodes[node_id].routing_table
    string += "Node #" + str(node_id) + " Routing Table:\n"
    string += "Dest_id : Next_id\n"
    for node in table:
        string += str(node) + " : " + str(table[node]) + "\n"

    return string

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
    print "Stopping simulation"

#start_demo()


