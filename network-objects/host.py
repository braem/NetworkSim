import Router
class Host (Router):
    def __init__(self):
        self.node_id = self.Node.node_id
        self.Node.node_id += 1

    def get_protocol_frame(self, message):
        #TODO this
        pass


    def wrap_new_protocol_frame(self, message, destination_id):
        #TODO this
        pass