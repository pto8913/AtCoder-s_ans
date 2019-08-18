import sys

sys.setrecursionlimit(10**6)

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())

g = []
counter = []
ans = []

def dfs(cur, par, val):
  global counter, ans, g
  val += counter[cur]
  ans[cur] = val
  for e in g[cur]:
    if e == par:
      continue
    dfs(e, cur, val)

def main():
  global g, ans, counter
  N, Q = na()
  
  g = [[] for _ in range(N)]
  for _ in range(N - 1):
    a, b = na()
    g[a-1] += [b-1]
    g[b-1] += [a-1]

  counter = [0] * N
  for _ in range(Q):
    p, x = na()
    counter[p-1] += x

  ans = [0] * N
  dfs(0, -1, 0)
  print(*ans)

if __name__ == "__main__":
  main()

""" 嘘解法
import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())

def main():
  N, Q = na()

  ab = []
  for _ in range(N-1):
    a, b = na()
    ab.append([a, b])
  ab.sort()

  counter = [0] * (N+1)
  for _ in range(Q):
    p, x = na()
    counter[p] += x
  for i in range(N - 1):
    counter[ab[i][1]] += counter[ab[i][0]]
  print(*counter[1:])

if __name__ == "__main__":
  main()
"""
