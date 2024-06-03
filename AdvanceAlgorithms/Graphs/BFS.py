''' Breadth first search in a graph'''

from collections import deque

def bfs(g, start):
    q = [start]
    visited = []
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            for item in g[node]:
                if item not in visited:
                    q.append(item)
    return visited

graph_ex = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(bfs(graph_ex, 'A'))
graph_ex = {
    '0': ['1', '3', '2'],
    '1': ['3'],
    '2': ['3'],
    '3': ['4'],
    '4': []
}
print(bfs(graph_ex, '0'))