graph = {
        '1': ['2','4'],
        '2': ['1','3'],
        '3': ['2','5'],
        '4': ['1','2'],
        '5': ['2','3']
    }


def bfs(graph, start, end):
    # type: (object, object, object) -> object
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        elif node not in visited:

            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                if adjacent == end:
                    return new_path

        visited.add(node)

print bfs(graph, '1', '5')
