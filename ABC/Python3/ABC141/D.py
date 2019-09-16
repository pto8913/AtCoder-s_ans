import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

import heapq

def main():
  n, m = an()
  a = [-int(x) for x in stdin.readline().split()]
  heapq.heapify(a)
  ans = 0
  for _ in range(m):
    x = heapq.heappop(a)
    heapq.heappush(a, x / 2)
  print(-sum(int(x) for x in a))

main()
