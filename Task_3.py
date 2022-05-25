class Node:
    def __init__(self, value):
        self.value = value
        self.colour = 0
        self.node_list = []


def main():
    input_file = open("INPUT.TXT")
    arr = []
    n, m = map(int, input_file.readline().split())
    for i in range(1, n + 1):
        arr.append(Node(i))
    for s in input_file.readlines():
        a, b = map(int, s.split())
        arr[a - 1].node_list.append(arr[b - 1])
    dfs(arr[0])
    print(0)


def dfs(vertex):
    vertex.colour = 1
    for cur in vertex.node_list:
        if cur.colour == 1:
            print(1)
            exit()
        if cur.colour == 0:
            dfs(cur)
    vertex.colour = 2


main()
