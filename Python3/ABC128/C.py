N, M = map(int,input().split())
KS = [list(map(int,input().split())) for _ in range(M)]
P = list(map(int,input().split()))

ans = 0
for i in range(1 << N):
  tmp = 1
  for j, b in enumerate(KS):
    if sum([1 for bb in b[1:] if (i >> (bb - 1)) & 1 == 1])%2 != P[j]:
      tmp = 0
      break
  if tmp:
    ans += 1
print(ans)
