H, W = map(int,input().split())
A = [[int(i) for i in input().split()]for _ in range(H)]

ans = 1e9
for y in range(H):
  for x in range(W):
    tmp = 0
    for h in range(H):
      for w in range(W):
        tmp += min(A[h][w]*abs(y-h), A[h][w]*abs(x-w))
    ans = min(ans, tmp)
print(ans)