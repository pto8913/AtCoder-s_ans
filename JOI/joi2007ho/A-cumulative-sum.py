N, K = map(int,input().split())
A = [int(input()) for _ in range(N)]

X = [0]*(N+1)
for i in range(N):
  X[i+1] = X[i]+A[i]

ans = -1e9
for i in range(N-K):
  ans = max(ans, X[i+K]-X[i])
print(ans)