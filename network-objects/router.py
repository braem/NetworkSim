import Switch
class Router (Switch):
    def __init__(self):
        self.node_id = self.Node.node_id
        self.Node.node_id += 1

    def get_ip_frame(self, message):
        #TODO this
        pass


    def wrap_new_ip_frame(self, message, destination_id):
        #TODO this
        pass
