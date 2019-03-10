# url: https://atcoder.jp/contests/abc108/tasks/arc102_a

N, K = map(int,input().split())
k = N//K
ans = k**3
if(K%2 == 0):
  if(k*K+K//2 <= N):
    ans += (k+1)**3
  else:
    ans *= 2
print(ans)
