# URL: https://atcoder.jp/contests/abc121/tasks/abc121_b

N, M, C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
for a in A:
  tmp = C
  for i in range(M):
    tmp += a[i]*B[i]
  if(tmp > 0):
    cnt += 1
print(cnt)
