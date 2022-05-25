from collections import deque
import sys

sys.stdin = open("INPUT.TXT")
sys.stdout = open("OUTPUT.TXT", 'w')

n = int(input())
graph = dict()
elem_set = set()
for i in range(n):
    elem_from, temp, elem_to = input().split()
    elem_set.add(elem_from)
    elem_set.add(elem_to)
    if elem_from not in graph:
        graph[elem_from] = set()
        graph[elem_from].add(elem_to)
    else:
        graph[elem_from].add(elem_to)

start_elem = input()
final_elem = input()

if start_elem == final_elem:
    print(0)
else:

    def BFS(start_vertex, graph, set_el):
        distances = dict()
        parents = dict()
        for vertex in set_el:
            distances[vertex] = None
            parents[vertex] = []
        distances[start_vertex] = 0
        queue = deque([start_vertex])
        while queue:
            cur_v = queue.popleft()
            if cur_v in graph:
                for neigh_v in graph[cur_v]:
                    if distances[neigh_v] is None:
                        distances[neigh_v] = distances[cur_v] + 1
                        parents[neigh_v].append(cur_v)
                        queue.append(neigh_v)
        return parents


    parents = BFS(start_elem, graph, elem_set)


    path = [final_elem]

    if final_elem in parents and parents[final_elem]:
        cur_parent = parents[final_elem][0]

        while parents[cur_parent]:
            path.append(cur_parent)
            cur_parent = parents[cur_parent][0]
        path.append(start_elem)
        print(len(path)-1)
    else:
        print(-1)




