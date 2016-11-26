from NetworkObjects.Node import Node
from NetworkObjects.Connection import Connection
from src.Network import Network


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
def dijkstra(graph, dest_node, source_node, visited=[], cost={}, previous={}):
    if source_node == dest_node:
        # if the very next hop is the destination
        path = []
        first_hop = dest_node
        while first_hop is not None:
            # add that hop to the path list
            path.append(first_hop)
            # none here will be the default result if there will be an error
            first_hop = previous.get(first_hop, None)
            x = str(path)
            y = str(cost[dest_node])
            return x
            # returns path and but we ae not showing cost
    else:
        # if not then search for the whole network
        if not visited:
            # initialise  the cost dict with 0
            cost[source_node] = 0
        # go through all the neighbors
        for neighbor in graph[source_node]:
            if neighbor not in visited:
                # new_cost will contain the sum of value in cost and the cost of source node's neighbour
                new_cost = cost[source_node] + graph[source_node][neighbor]
                # if new cost is smaller than calculated then update the cost dict with new min cost
                # float('inf') is representing infinity and it will be default result if the error will be generated
                #  that is cost will be infinity that case
                if new_cost < cost.get(neighbor, float('inf')):
                    cost[neighbor] = new_cost
                    previous[neighbor] = source_node
        # label it as visited and add into visited list
        visited.append(source_node)
        # now it will take into consideration the non visited one's
        # it has minimum latency and will match with minimum latency, to check there is any shorter path(small latency)
        # than the  one already calculated
        # run Dijkstra with source_id='shortest'
        unvisited = {}
        for k in graph:
            # if key is not in visited
            if k not in visited:
                unvisited[k] = cost.get(k, float('inf'))
        shortest = min(unvisited, key=unvisited.get)
        dijkstra(graph, dest_node, shortest, visited, cost, previous)


def convert_connections(graph):
    graph[Node.node_id] = {Network.connected, Connection.latency}
    return graph


if __name__ == "__main__":
    # graph= dict({[Node.node_id] = {Network.connected, Connection.latency}})
    # graph={}
    graph = convert_connections(graph={})

    dijkstra(graph, 'source_node', 'previous')
