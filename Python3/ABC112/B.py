# URL: https://atcoder.jp/contests/abc112/tasks/abc112_b

N, T = map(int,input().split())
ans = 1e9
for i in range(N):
  c, t = map(int,input().split())
  if(t <= T):
    ans = min(ans, c)
if(ans == 1e9):
  ans = "TLE"
print(ans)
