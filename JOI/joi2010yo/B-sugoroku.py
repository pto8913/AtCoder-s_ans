N, M = map(int,input().split())
masu = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]

cnt = 0
cur = 0
for i in range(M):
  if cur >= N:
    break
  cur += dice[i]
  if cur < N-1:
    cur += masu[cur]
  cnt += 1
print(cnt)