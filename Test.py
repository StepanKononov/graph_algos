from collections import deque

G = {'A': {'B', 'D', 'C'},
     'B': {'A', 'D', 'K'},
     'C': {'A', 'F', 'K'},
     'D': {'B', 'A', 'K'},
     'F': {'C', 'K'},
     'K': {'D', 'B', 'C', 'F', 'M'},
     'M': {'K'},
     'L': {}}


def DFS(start_vertex, graph, used):
    used.add(start_vertex)
    for neighbor in graph[start_vertex]:
        if neighbor not in used:
            DFS(neighbor, graph, used)




def BFS(start_vertex, graph):
    distances = dict()
    parents = dict()
    for vertex in graph:
        distances[vertex] = None
        parents[vertex] = []
    distances[start_vertex] = 0
    queue = deque([start_vertex])
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                parents[neigh_v].append(cur_v)
                queue.append(neigh_v)
    print(parents)
    return parents


parents = BFS("A", G)

end_vertex = "M"
path = [end_vertex]

cur_parent = parents[end_vertex][0]

while parents[cur_parent]:
    path.append(cur_parent)
    cur_parent = parents[cur_parent][0]

print(path)


