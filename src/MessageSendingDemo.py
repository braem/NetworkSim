from Segments.Segment import *
from Segments.Header import *
from Segments import IPDatagram
from Segments import EthernetFrame
from NetworkObjects.Node import *
from NetworkObjects import Connection
from SimulationLoop import *


import Network
import Packet

#First off, we need a network.

teh_matrix = Network()

#Sweeet.  Now we need a couple of host nodes.

host = Host()
hostess = Host()
teh_matrix.add_node(host)
teh_matrix.add_node(hostess)

#Define a simple step function to see if the simulation works.
def test_step(network):
    i = 0
    print "New Step"
    for packet in network.packets[:]:
        print "packet #" + i

        if packet.timer > 0:
            packet.decrement_timer()
        elif packet.timer == 0:
            network.packets.remove(packet)

        print "final timer value: " + packet.timer
        print "packet location is node" + packet.
        # else: Undecided.  This may indicate the packet should be removed
        i += 1


#Gender equality ftw.  Let's connect 'em up with some arbitrary latency.

wire = Connection(host, hostess, 5)
teh_matrix.add_connection(wire)

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

#Add packet to the packets list
teh_matrix.packets.append(packet)

#Create a SimThread that will run a little longer than the connection latency.
simulation = SimThread(test_step, teh_matrix, 10)

simulation.start()
simulation.join()



#Let's stop here and see if the message will move around as is.



