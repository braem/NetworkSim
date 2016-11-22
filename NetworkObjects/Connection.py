class Connection:
    next_connection = 0;
    def __init__(self, node1, node2, latency):

        self.connection_id = self.next_connection
        self.next_connection += 1
        self.nodes = [node1, node2]
        self.latency = latency

    def other_node(self, node):
        if node == self.nodes[0]:
            return self.nodes[1]
        else:
            return self.nodes[0]


