import sys

stdin = sys.stdin.readline
na = lambda: map(int, stdin().split())
ns = lambda: stdin().rstrip()
ni = lambda: int(ns())
def main():
  n = ni()
  b = list(na()) + [1e9]
  a = [b[0]]
  for i in range(n-1):
    a.append(min(b[i], b[i+1]))
  print(sum(a))
main()