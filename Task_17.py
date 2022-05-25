import sys


def main():
    sys.stdin = open("INPUT.TXT")
    sys.stdout = open("OUTPUT.TXT", 'w')

    n, m = map(int, input().split())
    inf = float('inf')

    graph = [[inf for j in range(n)] for i in range(n)]

    for i in range(m):
        town_1, town_2 = map(int, input().split())
        town_1 -= 1
        town_2 -= 1
        graph[town_1][town_2] = 0
        graph[town_2][town_1] = min(graph[town_2][town_1], 1)



    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j ] = min(graph[i][j], graph[i][k] + graph[k][j])

    ans = 0

    for i in range(n):
        for j in range(n):
            ans = max(ans, graph[i][j])
    print(ans)


main()