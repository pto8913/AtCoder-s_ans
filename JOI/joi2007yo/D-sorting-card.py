N = int(input())
M = int(input())
card = list(range(1,2*N+1))

for _ in range(M):
  k = int(input())
  if k == 0:
    tmp = []
    for a, b in zip(card[:N], card[N:]):
      tmp += [a]
      tmp += [b]
    card = tmp
  else:
    card = card[k:]+card[:k]
print("\n".join(list(map(str, card))))