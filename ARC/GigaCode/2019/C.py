import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

d = ni()
a = na()
b = na()

money = 0
ans = float('inf')
for i in range(d):
  money += a[i]
  if money >= b[i]:
    ans = min(ans, b[i])

if ans == float('inf'):
  ans = -1
print(ans)
