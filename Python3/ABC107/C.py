# URL: https://atcoder.jp/contests/abc107/tasks/arc101_a

N, K = map(int,input().split())
X = list(map(int,input().split()))

ans = 1e9
for l, r in zip(X, X[K-1:]):
  ans = min(ans, r-l+min(abs(l),abs(r)))
print(ans)
