"""Defines the Packet class"""
__author__ = "Rhys Beck"
__version__ = "1.0.0"

if __name__ == '__main__':
    class Packet:

        """This class is intended to wrap Ryan's Segment/Datagram/Frame for convenience in advancing the simulation."""

        '''Why is this here?

        Sprint 1: Right now, I need to keep track of:
            - what node the packet is at/is moving away from.
            - a packet-specific timer for connection delay.
        It makes no sense to store this information in the Network class.

        Sprint 2: Later on I'll also need to know if the packet is transmitting or propagating
        so I can tell what to do with it when the timer is up.
        '''

        def __init__(self, node, payload):
            self.connection = None
            self.payload = payload

        def set_connection(self, connection):
            self.connection = connection

        def set_timer(self, time):
            self.timer = time

        def decrement_timer(self):
            self.timer -= 1

        def update_packet_location(packet):
            pass

        '''    if packet.current_node != packet.get_destination():
                packet.deliver()  # just updates what node the packet thinks it's at
                packet.current_node.deliver(packet)

                # My guess is that node.deliver(packet) will begin the process of dealing
                # with a packet at a given node, for example put a link layer frame into the
                # node's link layer input buffer, but I have no idea how that will actually work.

            else:
                node.process_step()

                # This means the packet started this cycle at it's final destination...
                # What to do now depends on the implementation of the node classes.
                # Presumably the node classes have something in place to define how
                # packets are handled within a node.
        '''

        def deliver(self):
            self.current_node = self.connection.other_node(self.current_node)
            self.connection = None

        def get_destination(self):
            pass
        '''
            #extracts destination from the payload and returns it
            #This should probably behave contextually, extracting the destination from the outermost layer
            #of the payload.
       '''
