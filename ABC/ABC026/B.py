import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  pi = 3.14159265359
  n = ni()
  a = [ni() for _ in range(n)]
  a.sort()
  ans = 0
  for i, aa in enumerate(a, 1):
    if i % 2 == 0:
      ans -= aa ** 2
    else:
      ans += aa ** 2
  print(abs(ans * pi))

main()