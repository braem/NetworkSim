graph = {1: {2: 2, 3: 1},
         2: {3: 8},
         3: {1: 2, 4: 2},
         4: {5: 7, 6: 4},
         5: {6: 5},
         6: {3: 4}}


# def shortest_paths(graph, src, dst):
#     paths = []
#     graph_copy = graph.copy()
#     for source in graph.keys():
#         for dest in graph.keys():
#             if source != dest:
#                 paths.append(dijkstra(graph_copy, source, dest))
#                 del (graph_copy[source])
#         print paths


def dijkstra(graph, source_id, dest_id, visited=[], distances={}, parents={}):
    # Dijkstra's algorithm to calculate the shortest path
    # graph will have the connection and cost between nodes
    # dest_id will carry the address of destination node
    # source_id will have the address of source node
    # visited list will have list of all the visited nodes
    # cost dict will have the measured cost for each edge
    # parent dic will have all the neighbours of the node

    unvisited = [graph.keys()]

    if source_id == dest_id:
        # We build the shortest path and display it
        path = []
        distances[dest_id] = []
        parent = dest_id
        while parent != None:
            path.append(parent)
            parent = parents.get(parent, None)  # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
            print('shortest path: ' + str(path))
    else:
        # if it is the initial  run, initializes the cost and visited dict is empty
        if not visited:
            distances[source_id] = 0
        # visit the neighbors
        for neighbor in graph[source_id]:
            if neighbor not in visited:
                new_distance = distances[source_id] + graph[source_id][neighbor]
                # graph[source_id][neighbor] returns list of the nodes connected to source
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    parents[neighbor] = source_id  # source id will become parent
        # mark as visited
        visited.append(source_id)
        # now that all neighbors have been visited: recurse
        # unvisited.pop(source_id)
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:  # if key is not in visited dict
                unvisited[k] = distances.get(k, float('inf'))  # D.get(k[,d]) -> D[k] if k in D,defaults to infinity.
                # get the distances for all unvisited nodes and put it into unvisited dict with distances as values.
        # for getting minimum value out of those
        #  x = min(unvisited, key=unvisited.get)
        node_with_minvalue = min(unvisited, key=lambda k: unvisited[k])
        dijkstra(graph, node_with_minvalue, dest_id, visited, distances, parents)


if __name__ == "__main__":
    dijkstra(graph, 1, 6)
