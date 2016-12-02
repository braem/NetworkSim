"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"


from Node import *
from Connection import Connection
from SimulationLoop import *

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
                del(network.packets[packet.packet_id])
                print "packet", packet.packet_id, "has arrived at node", packet.current_node.node_id, "and been deleted."
        else:
            print "packet", packet.packet_id, "has neg timer, so it's just starting."
            packet.update_location()

        print "packet is at node " + str(packet.current_node.node_id)

def n_node_demo(n):
    """Creates a linear network of n Hosts, and sends a single Packet along the network."""

    #initialize global network variable
    Network.network_init()
    network = Network.network
    #Already have a global network instance, but it's empty.
    #Now we need a few host nodes.  Create a few linear networks and stitch them together
    #TODO add more network branches
    for j in range(0,n):

        previous = j - 1
        this = j
        network.add_node(Host())

        if previous >= 0:
            previous_node = network.nodes[previous]
            this_node = network.nodes[this]
            network.add_connection(previous_node.node_id, this_node.node_id, Connection(previous_node, this_node, 2))

    tables = routing_tables(network)

    #Set the routing tables in all the nodes
    for node in network.nodes.values():
        node.routing_table=tables[node.node_id]
        print node.node_id, node.routing_table

    for key in network.connections:
        print key, network.connections[key].connection_id

    #Create one message to start off
    network.create_messageUDP(0, n-1, "Message")

    # Create a SimThread that will run a little longer than the total connection and processing latency.
    simulation = SimThread(test_step, network, 50)
    print "Starting simulation"
    simulation.start()
    simulation.join()
    print "Simulation all done now =)"

n_node_demo(5)


