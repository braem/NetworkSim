"""Message Sending Demo"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

from Segments.Segment import *
from Segments.Header import *
from Segments import IPDatagram
from Segments import EthernetFrame
from NetworkObjects.Node import *
from NetworkObjects.Connection import Connection
from SimulationLoop import *


from Network import Network
from Packet import Packet


# Define a simple step function to see if the simulation works.
def test_step(network):
    i = 0
    print "New Step~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for packet in network.packets.values():
        print "packet #" + str(i)

        if packet.timer > 0:
            packet.decrement_timer()
        elif packet.timer == 0:
            packet.decrement_timer()
            packet.update_packet_location()
            #This implicitly assumes processing an arriving packet takes 1 time step.
        else:
            del(network.packets[packet.packet_id])

        print "final timer value: " + str(packet.timer)
        print "packet location is node " + str(packet.current_node.node_id)
        # else: Undecided.  This may indicate the packet should be removed
        i += 1


#First off, we need a network.

teh_matrix = Network()
#Sweeet.  Now we need a couple of host nodes.

host = Host()
hostess = Host()
teh_matrix.add_node(host)
teh_matrix.add_node(hostess)

#Gender equality ftw.  Let's connect 'em up with some arbitrary latency.

wire = Connection(host, hostess, 5)
teh_matrix.add_connection(host, hostess, wire)

#Okay, now we have a shoddy network.  Next we need a message to send.
#UDP seems easy. Let's do that.
#Source is host, destination is hostess (Using node_id's as "port numbers"
#Set the header length to zero just to be a defecatory disruptor.
uheader = UDPHeader(host.node_id, hostess.node_id, 0)
segment = UDPSegment(uheader, "I hates ur gutz")

#Put the segment in an IP datagram with a useless header
ip_datagram = IPDatagram("Dis be a IP header", segment)

#Put the datagram in an ethernet frame with a useless header
eth_frame = EthernetFrame("Dis be a ethernet header", ip_datagram)

#Put the frame in a Packet so the simulation knows what to do with it.
packet = Packet(host, eth_frame)

#Artificially set the packet's connection to the connection between host and hostess
packet.set_connection(wire)

#Add packet to the packets list
teh_matrix.packets[packet.packet_id] = packet

#Create a SimThread that will run a little longer than the connection latency.
simulation = SimThread(test_step, teh_matrix, 10)

print "Starting simulation"
simulation.start()
simulation.join()
print "Simulation all done now =)"





#Let's stop here and see if the message will move around as is.



