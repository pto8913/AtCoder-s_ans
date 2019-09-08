import sys

stdin = sys.stdin.readline
na = lambda: map(int, stdin().split())
ns = lambda: stdin().rstrip()
ni = lambda: int(ns())

def main():
  n, k = na()
  s = ns()

  ans = n-1
  for i in range(1, n):
    if s[i] != s[i-1]:
      ans -= 1
  print(min(n-1, ans+2*k))
main()