"""This file contains classes and functions for running the network simulation"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

import routing_table_algo
import threading
from src.Network import Network

class SimThread(threading.Thread):

    """The thread class to be instantiated to run the simulation

    USAGE NOTE: in order to stop a SimThread under normal usage, use SimThread.end().  This will allow
    the network's state to be saved by letting the current cycle (tick) finish before terminating."""

    #lock will be used to synchronize threads accessing the run flag.

    def __init__(self, function, args=(), the_end=-1):
        """Initializes a new SimThread which will run function(args) the_end times

        :type function function
        :type args tuple
        :type the_end integer"""

        threading.Thread.__init__(self)
        self.runFlag = True
        self.function = function
        self.args = args
        self.theEnd = the_end
        self.lock = threading.Lock()

    def run(self):
        """The run method executes function(args) theEnd times, or if theEnd < 0 runs until stopped

        function is a function to be called
        args is a tuple specifying the arguments to function, defaults to ()
        theEnd is an integer indicating how many times function should be performed, defaults to -1 (run forever)"""

        time = 0

        while (self.theEnd < 0 or time < self.theEnd) and self.access_flag():
            self.function(self.args)
            time += 1

    def access_flag(self, write=False, value=False):
        """Provides single read or write access to no more than one thread at a time.

        if write is true, value indicates what boolean value to set the run flag to.
        :type write: boolean
        :type value: boolean"""


        self.lock.acquire()

        if write:
            self.runFlag = value
            self.lock.release()
            return
        else:
            flag = self.runFlag
            self.lock.release()
            return flag

    def end(self):
        """Sets the runFlag to False, causing this SimThread to terminate once the current simulation cycle ends."""
        self.access_flag(write=True, value=False)


def sim_step(network):
    """This is the "step function" that will run the simulation ahead one tick.

    The idea is that a SimThread will loop through this either a specified number of times, or until
    it is told to stop. Each pass through the loop updates every network entity in sequence, decrementing wait counters
    and moving messages around as appropriate.

    :type network Network"""


    for packet in network.packets.values():
        if packet.timer > 0: packet.decrement_timer()
        else: packet.update_location(packet)

def start_simulation(network, function=sim_step, num=-1):
    """Starts a new thread to run the simulation with the given global network object

    returns a reference to the SimThread running the simulation so that the GUI thread
    can stop the simulation.

    SEE SimThread USAGE NOTE!!! (in SimThread class)
    :type network: Network
    :rtype SimThread"""

    #compute routing tables for each node
    tables=routing_table_algo.routing_tables(network)

    #insert routing tables into the nodes
    for node in network.nodes.values():
        node.routing_table = tables[node.node_id]


    thread = SimThread(function, args=network, the_end=num)
    thread.start()

    return thread


def tick():
    start_simulation(Network.network, 1)

    '''
    Rhys's Notes - Rough Outline

    For this bit, I'm assuming messages are not threads, because that idea is inconsistent with
    this approach.

    It must be assumed that the GUI thread has the power/authority/priority to preempt the
    thread running this loop in order to make changes to the network object.  I imagine this as
    a simple stop flag that the simulation thread checks every time a cycle is completed.  If the
    stop flag is set, the simulation thread should terminate.  This is okay if all modifications
    to the network, including creation/update/deletion of messages, are stored within the global
    network object, and so the network's state is saved.

    This way, the GUI can make whatever changes are needed while the simulation is halted, and then
    spawn a new thread to take up the simulation again once modifcations are complete.  This could
    probably be modified in a straightforward way to allow modifcation while appearing not to interrupt
    the simulation.


    What does the simulation loop do?:

        Iterates through all network entities and advances them one tick into the future.
        Since nodes and connections don't DO anything right now, this will pretty much
        solely involve moving messages around and deleting them once they reach their
        destinations.

    How is a message created?

        I'm currently assuming that the simulation thread doesn't create messages, the GUI thread does.
        This would simply mean setting the stop flag, then accessing the (thread-safe) network object
        and adding new messages at the nodes they are starting from.  Easy-peasy.

    What is a message?

        Properly, a message/packet is a nested object with a hierarchy like so:

        Message carried by Segment carried by Datagram carried by Frame

        Segment has transport layer header, which should specify source and destination port numbers, at the very least.
        Datagram has network layer header, which should specify source and destination IP addresses, at the very least.
        Frame  has link layer header, which should specify source and destination MAC addresses, at the very least.

        For the first sprint, however, it is reasonable to ignore some of the complexity of this picture
        and instead collapse this three layer addressing scheme to a single layer.  So going forward I will
        assume we are only dealing with host level communication, and so I only need to deal with port numbers
        (basically pretending they are IP addresses).

        Thus, I shall deal with messages of the form

        Message carried by Segment

        And that's it, for now.

    How does a message move around?

        A message must be associated with (located at) a node somehow. I have created a Packet class to accomplish this.

        Given this, we proceed as follows:

        Step 1: Where to go?
            Simple Scenario (First Sprint)
                - If the message is at a node:
                    - call node's forward(message) method to determine where the message should move to next.
                    - forward(message) must return the connection along which the message should be sent.
                    - Since there will only be routing in the first sprint, this will be provided by Navjot.
                - Set the message's current connection to the returned connection.

            More Realistic Scenario (Second Sprint)
                - If the message is at a layer three device
                    - call the node's route(message) method, which returns the next connection the message should use.
                    - this will be determined based on the network layer header.
                - If the message is at a layer two device
                    - call the node's forward(message) method which returns the next connection the message should use.
                    - Here, we will use the link layer header info to determine this, so this is not necessarily the
                      same as the routing algorithm Navjot is doing.
                - Either way, set the message's current connection to the one returned.

        Step 2: How long to take?
            - Look up the specified connection in the global network object (thank you, Barry).
                Simple Scenario (First Sprint):
                    - Connection will specify a single delay value
                    - Set countdown to this delay value (to be decremented each cycle until it reaches zero)
                    - When countdown is zero, update message location to the node at the other end of the connection

                More Realistic Scenario (Second Sprint):
                    - The connection should specify, in some way
                        - transmission delay (time to push the packet out onto the connection)
                            - probably just a straight up value in arbitrary time units
                        - propagation delay (time for packet to traverse the link)
                            - issue 8 specifies "medium" and "length" fields, which combine to determine this.
                - With this info we do the following:
                    - set a countdown to the transmission delay (to be decremented every cycle until it reaches zero)
                        - during this time, another message can not be transmitted down this connection
                    - when counton is zero, set another countdown to the propogation delay (again decrement each cycle)
                        -during this time, another message may be transmitted down this connection
                    - when countdown is zero, update message location to the device on the other end of the connection.


        Step 3: Where to now?
            If the message has reached it's final destination, the message is pushed up the network stack within the
            host, unwrappy stuff happens and the message is delivered to the currently imaginary application layer.  This
            comes under Jeremy's purview, as he is writing the Host, Router, and Switch classes.

            If we still have a ways to go, see Step 1.

        There is a small fly in the ointment here, in that logic may or may not need to be implemented to prevent
        more than one message from using a given connection simultaneously.  For the first sprint, this will be ignored.




    '''