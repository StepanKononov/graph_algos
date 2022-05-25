from collections import deque
import sys

sys.stdin = open("INPUT.TXT")
sys.stdout = open("OUTPUT.TXT", 'w')
n = int(input())
main_graph = dict()

for i in range(n):
    main_p = input()
    main_graph[main_p] = set()
    m = int(input())
    for j in range(m):
        main_graph[main_p].add(input())
    input()


def is_recursive_function(graph, function):
    queue = deque()
    visited = set()
    inqueue = set()

    queue.append(function)
    inqueue.add(function)

    while queue:
        c = queue.popleft()
        inqueue.remove(c)
        visited.add(c)
        for vertex in graph[c]:
            if vertex == function:
                return True
            if vertex not in visited and vertex not in inqueue:
                queue.append(vertex)
                inqueue.add(vertex)
    return False


for function in main_graph:
    if is_recursive_function(main_graph, function):
        print("YES")
    else:
        print("NO")
