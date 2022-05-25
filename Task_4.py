import sys

sys.stdin = open("INPUT.TXT")

n, m = map(int, input().split())
G = {i: set() for i in range(1, n + 1)}

visired = [False] * (n + 1)
ans = []

for i in range(m):
    verge_1, verge_2 = map(int, input().split())
    G[verge_1].add(verge_2)


def dfs(start, G, visited, ans):
    visited[start] = True

    for u in G[start]:
        if not visited[u]:
            dfs(u, G, visited, ans)
    ans.append(start)


for i in range(1, n + 1):
    if not visired[i]:
        dfs(i, G, visired, ans)

print(ans[::-1])
