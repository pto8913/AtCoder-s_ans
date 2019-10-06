# URL: https://atcoder.jp/contests/abc076/tasks/abc076_b

N = int(input())
K = int(input())

ans = 1
for i in range(N):
  ans = min(ans*2, ans+K)
print(ans)
