N, M = map(int,input().split())
AB = [[int(i) for i in input().split()]for _ in range(M)]
S = AB[:]
S.sort(reverse = True)
cur = 0
cost = 0
for a, b in S:
  if cur >= M-1:
    break
  if a >= N:
    cur += 1
  else:
    cost += N-a
    cur += 1
print(cost)