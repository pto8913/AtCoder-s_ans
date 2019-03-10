# URL: https://atcoder.jp/contests/abc117/tasks/abc117_c

N, M = map(int,input().split())
X = sorted(list(map(int,input().split())))
tmp = sorted([X[i+1]-X[i] for i in range(M-1)])
ans = sum(tmp[:M-N])
if(M <= N):
  ans = 0
print(ans)
