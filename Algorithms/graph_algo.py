__author__ = 'caynan'


def bfs(start, adj):
    level = {start: 0}
    parent = {start: None}
    i = 1
    # previous level, i - 1
    frontier = [start]
    # we still have nodes to visit
    while frontier:
        # next level, i
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

    return level, parent



