from collections import deque
import sys

sys.stdin = open("INPUT.TXT")

m, n = map(int, input().split())
graph = [[char for char in input()] for i in range(m)]

q_x, q_y, max_len = map(int, input().split())
l = [[-1 for i in range(n)] for j in range(m)]
q_x, q_y = q_x - 1, q_y - 1
q = deque()
l[q_x][q_y] = 0
q.append([q_x, q_y])

while q:
    cur = q.popleft()

    for elem_i in range(-1, 2):
        for elem_j in range(-1, 2):
            if elem_i * elem_i + elem_j * elem_j == 1:

                ni = cur[0] + elem_i
                nj = cur[1] + elem_j
                if l[ni][nj] == -1 and graph[ni][nj] == '0':
                    l[ni][nj] = l[cur[0]][cur[1]] + 1
                    q.append([ni, nj])

ans = 0

for i in range(4):
    m_x, m_y, exrtra = map(int, input().split())
    m_x, m_y = m_x - 1, m_y - 1

    if l[m_x][m_y] <= max_len and l[m_x][m_y] != -1:
        ans += exrtra
print(ans)
