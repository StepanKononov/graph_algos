from collections import deque
import time


def is_recursive(graph, procedure):
    queue = deque()
    visited = set()
    inqueue = set()
    queue.append(procedure)
    inqueue.add(procedure)
    while len(queue) > 0:
        c = queue.popleft()
        inqueue.remove(c)
        visited.add(c)
        for v in graph[c]:
            if v == procedure:
                return True
            if v not in visited and v not in inqueue:
                queue.append(v)
                inqueue.add(v)
    return False

def main():
    with open("input.txt") as fr:
        N = int(fr.readline())
        graph = {}
        res = []
        pcs = []

        for _ in range(N):
            procedure = fr.readline().strip()
            pcs.append(procedure)
            n = int(fr.readline())
            calls = [fr.readline().strip() for _ in range(n)]
            graph[procedure] = calls
            fr.readline()

        for procedure in pcs:
            res.append("YES" if is_recursive(graph, procedure) else "NO")
        with open("output.txt", "w") as output:
            output.write("\n".join(res))


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    print(time.perf_counter() - t_start)
