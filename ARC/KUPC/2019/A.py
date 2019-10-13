import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, x = na()
  a = na()

  max_a = max(a)
  cnt = 0
  for aa in a:
    if aa + x >= max_a:
      cnt += 1
  print(cnt)
main()