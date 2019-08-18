N = int(input())
V = list(map(int,input().split()))

V.sort()
ans = V[0]
for v in V[1:]:
  ans = (ans + v) / 2
print(ans)
