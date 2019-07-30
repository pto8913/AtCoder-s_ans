N = int(input())
score = [int(input()) for _ in range(N)]

sortScore = sorted(score, key = lambda x: -x)
rank = {}
ind = 1
for i in range(N):
  if sortScore[i] not in rank:
    rank[sortScore[i]] = ind
  ind += 1
for s in score:
  print(rank[s])