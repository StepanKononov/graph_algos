import sys

sys.stdin = open("INPUT.TXT")

n, m = map(int, input().split())
graph = {str(i): set() for i in range(1, n + 1)}

for i in range(m):
    verge_1, verge_2 = input().split()
    graph[verge_1].add(verge_2)
    graph[verge_2].add(verge_1)


used = dict()
colors = [1, 0]
def bipartite_graph_check(start_vertex, graph, used, color):
    used[start_vertex] = colors[color]
    for neighbor in graph[start_vertex]:
        if neighbor in used:
            if colors[color] == used[neighbor]:
                return False
        else:
            bipartite_graph_check(neighbor, graph, used, colors[color])
    return True


all_bipartite = True
for vertex in graph:
    if vertex not in used:
        all_bipartite = all_bipartite and bipartite_graph_check(vertex, graph, used, 0)
if all_bipartite:
    print(1)
else:
    print(0)