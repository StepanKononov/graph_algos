f = open("INPUT.TXT")
n = int(f.readline())
s = [list(map(int, i.split())) for i in f.readlines()]

a = dict()
for i in range(len(s)):
    a[i] = dict()

for i in range(len(s)):
    for j in range(len(s)):
        a[i][j] = ((s[i][0] - s[j][0]) ** 2 + (s[i][1] - s[j][1]) ** 2) ** 0.5
print(a)
ver_ready = set()
edges = set()
sum1 = 0
temp = 0
while len(ver_ready) != len(s):
    ver_ready.add(temp)
    for i in a[temp]:
        if i not in ver_ready:
            edges.add((a[temp][i], i))
    ans = min(edges, key=lambda k: k[0])
    while ans[1] in ver_ready and ans in edges:
        edges.remove(ans)
        if len(edges) != 0:
            ans = min(edges, key=lambda k: k[0])
    if ans[1] not in ver_ready:
        sum1 += ans[0]
        temp = ans[1]
print(sum1)
