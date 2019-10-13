import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, m = na()
  if n * 2 > m:
    print(m // 2)
  else:
    print(n + (m - n * 2) // 4)

main()