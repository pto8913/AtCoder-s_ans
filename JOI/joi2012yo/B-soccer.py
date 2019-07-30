N = int(input())
ABCD = [[int(i) for i in input().split()]for _ in range(N*(N-1)//2)]

team = list(range(1, N+1))
score = {i:0 for i in team}
for a, b, c, d in ABCD:
  if c > d:
    score[a] += 3
  elif c < d:
    score[b] += 3
  else:
    score[a] += 1
    score[b] += 1

tmp = max(score.values())
rank = {}
ind = 1
x = 0
for k, v in sorted(score.items(), key = lambda x: -x[1]):
  if v == tmp:
    rank[k] = ind
    x += 1
  else:
    ind += x
    rank[k] = ind
    x = 1
  tmp = v

for t in team:
  print(rank[t])