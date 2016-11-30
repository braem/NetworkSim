"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

from Segments.Header import *
from Segments import IPDatagram
from Segments import EthernetFrame
from Node import *
from Connection import Connection
from SimulationLoop import *

from Network import network
from Packet import Packet


def test_step(network):
    """Step function for use in the simulation"""
    i = 0
    print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for packet in network.packets.values():
        print "packet #" + str(i)
        print "initial timer value: " + str(packet.timer)

        if packet.timer > 0:
            packet.decrement_timer()
        elif packet.timer == 0:
            packet.decrement_timer()
            packet.update_location()
            next_connection = get_next_connection(packet)

            if(next_connection == packet.connection):
                del(network.packets[packet.packet_id])
                print "packet", packet.packet_id, "has been deleted."
            else: packet.set_connection(get_next_connection(packet))
            #THIS IS NOT good.  For demo purposes only.  See function definition below.

            #This implicitly assumes processing an arriving packet takes 1 time step.
        else:
            del(network.packets[packet.packet_id])


        print "packet location is node " + str(packet.current_node.node_id)
        # else: Undecided.  This may indicate the packet should be removed
        i += 1

def n_node_demo(n):
    """Creates a linear network of n Hosts, and sends a single Packet along the network."""

    # First off, we need a network.

    global teh_matrix
    teh_matrix = network
    # Sweeet.  Now we need a few host nodes.


    for j in range(0,n):

        previous = j - 1
        this = j
        teh_matrix.add_node(Host())

        if previous >= 0:
            previous_node = teh_matrix.nodes[previous]
            this_node = teh_matrix.nodes[this]
            teh_matrix.add_connection(previous_node, this_node, Connection(previous_node, this_node, 2))




    uheader = UDPHeader(teh_matrix.nodes[0].node_id, teh_matrix.nodes[n-1].node_id, 0)
    segment = UDPSegment(uheader, "I hates ur gutz")

    # Put the segment in an IP datagram with a useless header
    ip_datagram = IPDatagram("Dis be a IP header", segment)

    # Put the datagram in an ethernet frame with a useless header
    eth_frame = EthernetFrame("Dis be a ethernet header", ip_datagram)

    # Put the frame in a Packet so the simulation knows what to do with it.
    packet = Packet(teh_matrix.nodes[0], eth_frame)

    # Artificially set the packet's connection to the first connection.
    packet.set_connection(teh_matrix.connections[0]["connection"])

    # Add packet to the packets list
    teh_matrix.packets[packet.packet_id] = packet

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


def get_next_connection(packet):
    # I  want to be very very clear.  This is NOT how this is meant to work.  IT's just a quick little work-around to
    # make things happen since I don't have access to the storied routing bits.
    current_connection = packet.connection.connection_id
    number_of_connections = len(teh_matrix.connections)

    if(current_connection < number_of_connections - 1):
        return teh_matrix.connections[current_connection + 1]["connection"]
    else: return packet.connection




n_node_demo(5)


