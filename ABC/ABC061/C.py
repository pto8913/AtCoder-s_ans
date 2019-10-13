import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, k = na()
  ab = [na() for _ in range(n)]
  ab.sort(key = lambda x: x[0])
  cnt = 0
  for a, b in ab:
    cnt += b
    if cnt >= k:
      print(a)
      return

main()