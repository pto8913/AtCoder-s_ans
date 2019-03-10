# URL: https://atcoder.jp/contests/abc115/tasks/abc115_c

N, K = map(int,input().split())
H = sorted([int(input()) for _ in range(N)])
ans = 1e9
for i in range(N-K+1):
  ans = min(ans, H[i+K-1]-H[i])
print(ans)
