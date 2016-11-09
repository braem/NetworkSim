def bfs(graph, start, end):
    routerqueue = [[start]]
    visited = set()

    while routerqueue:
        path = routerqueue.pop(0)
        node = path[-1]
        if node == end:
            return path
        elif node not in visited:

            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                routerqueue.append(new_path)

    graph = {
        '1': ['2','4'],
        '2': ['3'],
        '3': ['2','4'],
        '4': ['1','3']
    }

    print bfs(graph, '1', '3')
