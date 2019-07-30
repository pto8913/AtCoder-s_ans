N, M = map(int,input().split())
A = [int(input()) for _ in range(N)]

for k in range(2, M+1):
  for i in range(N-1):
    if i+1 != N:
      if A[i]%k > A[i+1]%k:
        A[i], A[i+1] = A[i+1], A[i]
print("\n".join(list(map(str, A))))