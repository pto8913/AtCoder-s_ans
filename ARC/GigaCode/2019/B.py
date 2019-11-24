import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

n, x, y, z = na()

ans = 0
for _ in range(n):
  a, b = na()
  if a >= x and b >= y and a + b >= z:
    ans += 1
print(ans)