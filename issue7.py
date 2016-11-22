from Node import Node
from Connection import Connection
from Network import Network

class Graph:
    # graph dict is calling the Node class and Network to get the connection between the nodes and latency will be cost
    #  between the two nodes and path with min delay will be chosen as shortest path
    def __init__(self):
       pass

   # def connection_network(self, graph):
    #    self.graph[Node.node_id] = {Network.connected, Connection.latency}


# graph = {'s': {'a': 2, 'b': 1},
#  'a': {'s': 3, 'b': 4, 'c': 8},
# 'b': {'s': 4, 'a': 2, 'd': 2},
#  'c': {'a': 2, 'd': 7, 't': 4},
# 'd': {'b': 1, 'c': 11, 't': 5},
# 't': {'c': 3, 'd': 5}}


# Dijkstra's algorithm to calculate the shortest path
# graph will have the connection and cost between nodes
# destination_id will carry the address of destination node
# source_id will have the address of source node
# visited list will have list of all the visited nodes
# Cost dict will have the measured cost for each edge
# predecessors dic will have all the neighbours of the node


def dijkstra(graph, destination_id, source_id, visited=[], cost={}, predecessors={}):
    if source_id == destination_id:
        # The very next hop is the destination
        path = []
        first_hop = destination_id
        while first_hop != None:
            path.append(first_hop)
            first_hop = predecessors.get(first_hop, None)
            x = str(path)
            y = str(cost[destination_id])
            return x, y
            # returns path and cost counted for that path
    else:
        # if not then search for the whole network
        if not visited:
            cost[source_id] = 0
        # go through all the neighbors
        for neighbor in graph[source_id]:
            if neighbor not in visited:
                new_distance = cost[source_id] + graph[source_id][neighbor]
                if new_distance < cost.get(neighbor, float('inf')):
                    cost[neighbor] = new_distance
                    predecessors[neighbor] = source_id
        # label it as visited and add into visited list
        visited.append(source_id)
        # now it will take into consideration the non visited one's
        # it has minimum latency and will match with minimum latency, to check there is any shorter path(small latency)
        # than the  one already calculated
        # run Dijkstra with source_id='shortest'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = cost.get(k, float('inf'))
        shortest = min(unvisited, key=unvisited.get)
        dijkstra(graph, destination_id, shortest, visited, cost, predecessors)


def connection_network(graph):
    graph[Node.node_id] = {Network.connected, Connection.latency}
    return graph


if __name__ == "__main__":
    # graph= dict({[Node.node_id] = {Network.connected, Connection.latency}})
    #graph={}
    graph=connection_network(graph={})

    dijkstra(graph, 'source_id', 'destination_id')
