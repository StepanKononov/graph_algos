import sys

sys.stdin = open("INPUT.TXT")

n, m = map(int, input().split())

graph = {str(i): set() for i in range(1, n + 1)}

for i in range(m):
    verge_1, verge_2 = input().split()
    graph[verge_1].add(verge_2)
    graph[verge_2].add(verge_1)
u, v = input().split()


def DFS(start_vertex, graph, used):
    used.add(start_vertex)
    for neighbor in graph[start_vertex]:
        if neighbor not in used:
            DFS(neighbor, graph, used)


n = 0
used = set()

DFS(u, graph, used)

if v not in used:
    print(0)
else:
    print(1)
