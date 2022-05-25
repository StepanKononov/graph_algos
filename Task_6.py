from collections import deque
import sys

sys.stdin = open("INPUT.TXT")

n, m = map(int, input().split())
graph = {str(i): set() for i in range(1, n + 1)}

for i in range(m):
    verge_1, verge_2 = input().split()
    graph[verge_1].add(verge_2)
    graph[verge_2].add(verge_1)
u, v = input().split()


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
    #print(parents)
    return parents


parents = BFS(v, graph)

end_vertex = u
path = [end_vertex]

if parents[end_vertex]:
    cur_parent = parents[end_vertex][0]

    while parents[cur_parent]:
        path.append(cur_parent)
        cur_parent = parents[cur_parent][0]
    path.append(v)
    print(len(path)-1)
else:
    print(-1)


