''' Breadth first search in a graph'''

from collections import deque

def dfs(g, start, visited):
    q = [start]
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            for item in g[node]:
                dfs(g, item,visited)
    return visited

graph_ex = {
    'A': ['B', 'C'],
    'B': ['C', 'E'],
    'C': ['D'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(dfs(graph_ex, 'A',[]))
graph_ex = {
    '0': ['1', '2'],
    '1': ['3'],
    '2': ['3'],
    '3': ['4'],
    '4': []
}
print(dfs(graph_ex, '0', []))