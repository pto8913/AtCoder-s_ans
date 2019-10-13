import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  a = na()
  mod = int(1e9+7)

  if n % 2 == 0 and len(set(a)) == n // 2:
    print(2 ** (n // 2) % mod)
  elif n % 2 == 1 and a.count(0) == 1:
    print(2 ** ((n - 1) // 2) % mod)
  else:
    print(0)
main()