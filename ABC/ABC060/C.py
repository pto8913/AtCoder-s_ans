import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, T = na()
  t = na()

  cnt = T
  for i in range(n - 1):
    cnt += min(T, t[i + 1] - t[i])
  print(cnt)

main()