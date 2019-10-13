import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

sys.setrecursionlimit(10**6)

def main():
  n, m = na()
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    a, b = na()
    graph[a] += [b]
    graph[b] += [a]
  
  def dfs(e, reach):
    if all(reach):
      return True

    ret = 0
    for e in graph[e]:
      if reach[e - 1]:
        continue
      reach[e - 1] = True
      ret += dfs(e, reach)
      reach[e - 1] = False
    return ret

  reach = [False] * n
  reach[0] = True
  print(dfs(1, reach))

main()