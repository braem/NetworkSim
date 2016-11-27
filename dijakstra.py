graph = {1: {2: 2, 3: 1},
         2: {1: 2, 3: 4, 4: 3},
         3: {1: 1, 4: 6},
         4: {3: 6, 6: 11,5: 10,7: 5},
         5: {4: 10, 6: 9},
         6: {4: 11, 5: 9, 7: 7, 8: 8},
         7: {6: 7, 4: 5},
         8: {6: 8}}

def dijkstra(graph, source_id, dest_id, visited=[], distances={}, parents={}):
    # Dijkstra's algorithm to calculate the shortest path
    # graph will have the connection and cost between nodes
    # dest_id will carry the address of destination node
    # source_id will have the address of source node
    # visited list will have list of all the visited nodes
    # cost dict will have the measured cost for each edge
    # parent dic will have all the neighbours of the node

    if source_id == dest_id:
        # We build the shortest path and display it
        path = []
        distances[dest_id] = []
        parent = dest_id
        while parent is not None:
            path.append(parent)
            parent = parents.get(parent, '*****')  # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

        #return path
        print str(path)
            # print('visited path: ' + str(visited))
    else:
        # if it is the initial  run, initializes the cost and visited dict is empty
        if not visited:
            distances[source_id] = 0
        # visit the neighbors
        for neighbor in graph[source_id]:
            if neighbor not in visited:
                new_distance = distances[source_id] + graph[source_id][neighbor]
                # graph[source_id][neighbor] returns cost of the nodes connected to source g[u][v]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance # replace existed distance with new distance
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
                unvisited[k] = distances.get(k, float('inf'))
                # D.get(k[,d]) -> D[k] if k in D,defaults to infinity.
                # get the distances for all unvisited nodes and put it into unvisited dict with distances as values.
                # for getting minimum value out of those
                #  x = min(unvisited, key=unvisited.get)
                node_with_minvalue = "NoNode"
                #if len(unvisited)==0:
                #   node_with_minvalue=dest_id
            #else:
                node_with_minvalue = min(unvisited, key=lambda k: unvisited[k])
                dijkstra(graph, node_with_minvalue, dest_id, visited, distances, parents)


if __name__ == "__main__":
    dijkstra(graph,1,5)
