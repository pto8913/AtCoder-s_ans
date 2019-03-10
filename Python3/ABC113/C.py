# URL: https://atcoder.jp/contests/abc113/tasks/abc113_c

N, M = map(int,input().split())
PY = [list(map(int,input().split()))+[0] for _ in range(M)]
sort_PY = sorted(PY, key = lambda x:x[1])
city = {}
for i in range(M):
  p, y = sort_PY[i][0], sort_PY[i][1]
  if(p in city):
    city[p] += 1
  else:
    city[p] = 1
  sort_PY[i][2] = city[p]
for p, y, z in PY:
  print(str(p).zfill(6)+str(z).zfill(6))
