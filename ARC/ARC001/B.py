import sys

sys.setrecursionlimit(100000000)

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

from collections import deque

def main():
  a, b = an()

  res = [-1] * 52

  que = deque()
  que.append(a)
  res[a] = 0

  while que:
    v = que.popleft()

    for t in [1, 5, 10, -1, -5, -10]:
      x = v + t
      if x < 0 or x >= 52:
        continue
      if res[x] != -1:
        continue
      res[x] = res[v] + 1
      que.append(x)
    if res[b] != -1:
      break
  print(res[b])

main()
