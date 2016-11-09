class Network:
    def __init__(self):
        self.nodes = {}
        self.connections = {}

        def add_node(self, node):
            """
            add a node to the network
            """
            self.nodes[node.node_id] = node

        def add_connection(self, n1_id, n2_id, connection):
            """
            add a connection between two nodes (by id)
            """
            self.connections[connection.connection_id] = {"nodes": sorted([n1_id, n2_id]), "connection": connection}

        def remove_node(self, node_id):
            """
            remove a node by id
            """
            try:
                del self.nodes[node_id]
                for c_id, connection in self.connections.iteritems():
                    if node_id in connection["nodes"]:
                        del self.connections[c_id]
                return True
            except:
                return False

        def remove_connection(self, c_id):
            """
            remove a connection by id
            """
            try:
                del self.connections[c_id]
                return True
            except:
                return False

        def get_connected_nodes(self, node_id):
            """
            returns a list of nodes connected to the given node in the form
            [{"node": the node at the other end, "connection": the connection object}]
            """
            connected = []
            for connection in self.connections.values():
                if node_id in connection["nodes"]:
                    other_node = connection["nodes"][0] if node_id == connection["nodes"][0] else connection["nodes"][1]
                    connected.append({"node":other_node, "connection":connection["connection"]})
            return connected
