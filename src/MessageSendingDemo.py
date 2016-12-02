"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"


from Node import *
from Connection import Connection
from SimulationLoop import *

from Network import network
from routing_table_algo import routing_tables


def test_step(network):
    """Step function for use in the simulation"""

    print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for packet in network.packets.values():
        print "packet #" + packet.packet_id


        if packet.timer > 0:
            print "transmitting on connection", packet.connection.connection_id
            print "Time steps to completion: " + str(packet.timer)
            packet.decrement_timer()
        elif packet.timer == 0:
            packet.decrement_timer()
            packet.update_location()

            print "packet", packet.packet_id, "has been forwarded onto connection", packet.connection.connection_id,\
                "latency:", packet.connection.latency, "."

            if(packet.get_destination() == packet.current_node):
                del(network.packets[packet.packet_id])
                print "packet", packet.packet_id, "has arrived at node", packet.current_node.node_id, "and been deleted."

        else:
            del(network.packets[packet.packet_id])

        print "packet is at node " + str(packet.current_node.node_id)

def n_node_demo(n):
    """Creates a linear network of n Hosts, and sends a single Packet along the network."""

    # First off, we need a network.

    global teh_matrix
    teh_matrix = Network()



    #Now we need a few host nodes.  Create a few linear networks and stitch them together
    #TODO add more network branches
    for j in range(0,n):

        previous = j - 1
        this = j
        teh_matrix.add_node(Host())

        if previous >= 0:
            previous_node = teh_matrix.nodes[previous]
            this_node = teh_matrix.nodes[this]
            teh_matrix.add_connection(previous_node, this_node, Connection(previous_node, this_node, 2))

    if isinstance(teh_matrix, Network): print "yup"
    else: print "nope"

    tables = routing_tables(teh_matrix)


    for node in teh_matrix.nodes.values():
        node.routing_table=tables[node.node_id]

    print "Node0", teh_matrix.nodes[0]
    #Create one message to start off
    teh_matrix.create_messageUDP(0, n, "Message")

    # Create a SimThread that will run a little longer than the total connection and processing latency.
    simulation = SimThread(test_step, teh_matrix, n * 3 + 5)


    print "nodes"
    print teh_matrix.nodes
    print "connections"
    print teh_matrix.connections

    print "Starting simulation"
    simulation.start()
    simulation.join()
    print "Simulation all done now =)"

n_node_demo(5)


