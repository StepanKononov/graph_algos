from collections import deque
import sys

sys.stdin = open("INPUT.TXT")
sys.stdout = open("OUTPUT.TXT", 'w')

check = "#"
uncheck = "."

n, m = map(int, input().split())

graph = [[elem for elem in input()] for i in range(n)]

move_x = [-1, 0, 1, 0]
move_y = [0, -1, 0, 1]


def correct(x, y):
    if x < 0 or y < 0:
        return False
    if x >= n or y >= m:
        return False
    return True


def DFS(fx, fy):
    s = deque()
    s.append([fx, fy])
    while s:
        cur = s.popleft()
        for i in range(4):
            x = cur[0] + move_x[i]
            y = cur[1] + move_y[i]

            if correct(x, y) and graph[x][y] == check:
                graph[x][y] = uncheck
                s.append([x, y])


def main():
    amount = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == check:
                DFS(i, j)
                amount += 1
    print(amount)


main()
