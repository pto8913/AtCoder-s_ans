import sys
from collections import defaultdict

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

def main():
  n, k = an()
  dp = defaultdict(lambda : float("inf"))
  dp[2019] = 0
  for _ in range(n):
    a, b = sn().split()
    a = int(a)
    d = list(dp.keys())
    if b == "F":
      d.sort(reverse=True)
      for i in d:
        dp[i + a] = min(dp[i + a], dp[i] + 1)
    else:
      d.sort()
      for i in d:
        dp[i - a] = min(dp[i - a], dp[i] + 1)
  if dp[k] == float("inf"):
    print(-1)
  else:
    print(dp[k])

main()
