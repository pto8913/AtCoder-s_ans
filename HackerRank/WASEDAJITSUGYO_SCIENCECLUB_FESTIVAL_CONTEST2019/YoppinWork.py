import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  t, n = na()
  ab = [na() for _ in range(n)]
  ab.sort(key = lambda x: (-x[0],-x[1]))
  ta, tb = ab[0]
  cnt = 1
  for a, b in ab[1:]:
    if b <= ta:
      cnt += 1
      ta = a
    
  print(cnt)
main()