import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def BFS(K, edges, N):
    roots = [[] for i in range(N)]
    for a, b in edges:
        roots[a-1] += [b-1]
        roots[b-1] += [a-1]
    dist = [-1] * N
    stack = []
    stack.append(K)
    dist[K] = 0
    while stack:
        label = stack.pop(-1)
        for i in roots[label]:
            if dist[i] == -1:
                if (dist[i] != 3):
                    dist[i] = dist[label] + 1
                    stack += [i]
    return dist

def main():
    N = ni()
    ab = [na() for _ in range(N)]
    distance = BFS(0, ab, N)
    for i in range(1, N+1):
        dist = distance[i]


if __name__ == '__main__':
    main()