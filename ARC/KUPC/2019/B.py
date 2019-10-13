import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def f(x, y, W):
  dp = [[0 for _ in range(W + 5)] for _ in range(W + 5)]
  for i in range(len(x)):
    for j in range(W + 1):
      if j >= y[i]:
        dp[i + 1][j] = max(dp[i][j - y[i]] + x[i], dp[i][j])
      else:
        dp[i + 1][j] = dp[i][j]
  return max(max(a for a in dp))

def main():
  n, m, W = na()
  v, w = [], []
  for _ in range(n):
    x, y = na()
    w.append(x)
    v.append(y)
 
  ab = []
  ww = []
  for _ in range(m):
    a, b = na()
    a -= 1
    b -= 1
    ab.append(v[a] + v[b])
    ww.append(w[a] + w[b])
  ab.sort(reverse=True)

  if m != 0:
    print(f(ab, ww, W))
  else:
    print(sum(v))
main()