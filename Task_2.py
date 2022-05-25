import sys

sys.stdin = open("INPUT.TXT")

n, m = map(int, input().split())
graph = {str(i): set() for i in range(1, n + 1)}

for i in range(m):
    verge_1, verge_2 = input().split()
    graph[verge_1].add(verge_2)
    graph[verge_2].add(verge_1)


def DFS(start_vertex, graph, used):
    used.add(start_vertex)
    for neighbor in graph[start_vertex]:
        if neighbor not in used:
            DFS(neighbor, graph, used)


used = set()
N = 0
for vertex in graph:
    if vertex not in used:
        DFS(vertex, graph, used)
        N += 1
print(N)
