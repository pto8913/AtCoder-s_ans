import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, m = na()
  a = na()
  b = na()
  d = {}
  for i, aa in enumerate(a):
    for j, bb in enumerate(b):
      if aa+bb in d:
        s, t = d[aa+bb]
        print(s, t, i, j)
        sys.exit()
      else:
        d[aa+bb] = (i, j)
  print(-1)
main()
