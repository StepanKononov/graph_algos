import sys


sys.stdin = open("INPUT.TXT")
sys.stdout = open("OUTPUT.TXT", 'w')
n, m = map(int, input().split())
maze = [[0 for j in range(100 + 1)] for i in range(n+1)]

for i in range(m):
    room1, room2, color = map(int, input().split())
    maze[room1][color] = room2
    maze[room2][color] = room1
l = input()
cur = 1
path = list(map(int, input().split()))
for color in path:
    cur = maze[cur][color]
if cur == 0:
    print("INCORRECT")
else:
    print(cur)