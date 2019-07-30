N, M = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(M)]

Lma = 0
Rmi = N + 1
for L, R in LR:
  Lma = max(L, Lma)
  Rmi = min(R, Rmi)

print(max(0, Rmi - Lma + 1))
