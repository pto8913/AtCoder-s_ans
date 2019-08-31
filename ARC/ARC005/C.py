import sys

sys.setrecursionlimit(100000000)

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

h, w = na()

c = []
for _ in range(h):
  c.append(ns())

reach = [[False]*w for _ in range(h)]

def dfs(y, x):
  if y < h and x < w and c[y][x] == "#":
    return dfs(y, x+1)
  
  reach[y][x] = True