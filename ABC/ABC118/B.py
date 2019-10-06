# URL: https://atcoder.jp/contests/abc118/tasks/abc118_b

N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(1,M+1):
  cnt = 0
  for a in A:
    if(i in a[1:]):
      cnt += 1
  if(cnt == N):
    ans += 1
print(ans)
