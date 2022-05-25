# Bellman–Ford Algorithm
import sys

sys.stdin = open("INPUT.TXT")


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.vertices
        dist[src] = 0

        for _ in range(self.vertices - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:

            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[u] = 0
                dist[v] = 0

        g.print_array(dist, src)

    def print_array(self, dist, start):

        for i in range(self.vertices):
            if dist[i] != float("inf"):
                if i == start:
                    print(0)
                elif dist[i] == 0:
                    print("-")
                else:
                    print(dist[i])
            else:
                print("*")


n, m = map(int, input().split())
g = Graph(n)

for i in range(m):
    u, v, w = map(int, input().split())
    g.graph.append([u-1, v-1, w])

start = int(input())-1
g.bellman_ford(start)
