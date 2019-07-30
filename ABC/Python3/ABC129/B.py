N = int(input())
W = list(map(int,input().split()))

ans = 1e9
for i in range(N):
  l = sum(W[:i+1])
  r = sum(W[i+1:])
  ans = min(ans, abs(l-r))
print(ans)
