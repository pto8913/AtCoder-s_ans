N, D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]

ans = 0
x = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(D):
      x += abs(X[i][k] - X[j][k])**2
    x = x**0.5
    if x == int(x):
      ans += 1
    x = 0
print(ans)
