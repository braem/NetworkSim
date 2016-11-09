"""Header.py: Defines headers for use in Segments"""
__author__ = "Ryan Paulitschke"
__version__ = "1.0.0"


# Parent Header
class Header:
    def __init__(self, source_port, destination_port, header_length):
        self.src_port = source_port
        self.dest_port = destination_port
        self.length = header_length
        self.checksum = None

    # default print notation when printing a header
    def __str__(self):
        return "src/dest port: %s/%s, length: %s, checksum: %s" % (
            self.src_port, self.dest_port, self.length, self.checksum)


# Header for UDP Segments
class UDPHeader(Header):
    def __init__(self, source_port, destination_port, header_length):
        Header.__init__(self, source_port, destination_port, header_length)
        self.checksum = (~(self.src_port + self.dest_port + self.length) + 1) % 65535

    # Calculates the checksum value for the header
    # Call after any changes to the ports or length are made
    def updateChecksum(self):
        self.checksum = (~(self.src_port + self.dest_port + self.length) + 1) % 65535
        return

    # Returns true if packet is deemed undamaged (checksum succeeds)
    # For this to work correctly ports & length should be ints between [0,65535]
    def checkChecksum(self):
        if (self.checksum + (self.src_port + self.dest_port + self.length) % 65535) == 65535:
            return True
        else:
            return False


# Header for TCP Segments
# Accepts 3 args if you only want to init ports & length
# Accepts 7 args if you also want to define sequence#, acknowledgemnt#, window size, and urgent data pointer
class TCPHeader(Header):
    def __init__(self, source_port, destination_port, header_length, sequence_number=None, acknowledgement_number=None, window=None, urgent_data_ptr=None):
        Header.__init__(self, source_port, destination_port, header_length)
        if sequence_number is None or acknowledgement_number is None or window is None or urgent_data_ptr is None:
            self.sequence_num = None
            self.ack_num = None
            self.receive_window = 0
            self.urgent_data_pointer = 0
            self.checksum = (~(
                self.src_port + self.dest_port + self.receive_window + self.urgent_data_pointer) + 1) % 65535
        else:
            self.sequence_num = sequence_number
            self.ack_num = acknowledgement_number
            self.receive_window = window
            self.urgent_data_pointer = urgent_data_ptr
            self.checksum = (~(
                self.src_port + self.dest_port + self.receive_window + self.urgent_data_pointer) + 1) % 65535

        # flag field
        self.urg = None
        self.ack = None
        self.psh = None
        self.rst = None
        self.syn = None
        self.fin = None

    # Sets the values for the flag field
    def updateFlagField(self, urg, ack, psh, rst, syn, fin):
        self.urg = urg
        self.ack = ack
        self.psh = psh
        self.rst = rst
        self.syn = syn
        self.fin = fin
        return

    # Calculates the checksum value for the header
    # Call after any changes to the ports or length are made
    def updateChecksum(self):
        self.checksum = (~(self.src_port + self.dest_port + self.receive_window + self.urgent_data_pointer) + 1) % 65535
        return

    # Returns true if packet is deemed undamaged (checksum succeeds)
    # For this to work correctly variables should be ints between [0,65535]
    def checkChecksum(self):
        if (self.checksum + (
                            self.src_port + self.dest_port + self.receive_window + self.urgent_data_pointer) % 65535) == 65535:
            return True
        else:
            return False

    # default print notation when printing a header (Doesn't print Flag Field)
    def __str__(self):
        return "src/dest port: %s/%s, length: %s, checksum: %s, seq#: %s, ack#: %s, window: %s, urgent ptr: %s" % (
            self.src_port, self.dest_port, self.length, self.checksum, self.sequence_num, self.ack_num,
            self.receive_window, self.urgent_data_pointer)
