import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

INF = int(1e9+7)

def dijkstra(s,n,w,cost, k):
    d = [INF] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        for i in range(k, n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True
               
        for j in range(k, n):
            d[j] = min(d[j],d[v]+cost[v][j])
    return d

def main():
    n, x, y = na()

    cost = [[INF for i in range(n)] for i in range(n)] 
    for i in range(n-1):
        cost[i][i+1] = 1
        cost[i+1][i] = 1
    cost[x-1][y-1] = 1
    cost[y-1][x-1] = 1

    ans = dict()
    kyo = 1
    for i in range(n):
        for s in dijkstra(i, n, n-1, cost, kyo):
            if s in ans:
                ans[s] += 1
            else:
                ans[s] = 1
        kyo += 1
    
    for i in range(n-1):
        if i+1 in ans:
            print(ans[i+1])
        else:
            print(0)

if __name__ == '__main__':
    main()