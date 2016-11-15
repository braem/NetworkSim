import Node
class Switch (Node):
    def __init__(self):
        self.node_id = self.Node.node_id
        self.Node.node_id += 1

    def get_ethernet_frame(self, message):
        #TODO this
        pass


    def wrap_new_ethernet_frame(self, message, destination_id):
        #TODO this
        pass