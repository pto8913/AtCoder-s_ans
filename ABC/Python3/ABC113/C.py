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

# import sys

# stdin = sys.stdin

# sn = lambda : stdin.readline().rstrip()
# an = lambda : map(int, stdin.readline().split())
# ni = lambda : int(sn())

# n, m = an()
# py = []
# for _ in range(m):
#   py.append(list(an()) + [0])

# sortPy = sorted(py, key = lambda x : (x[0], x[1]))

# d = {}
# for i, (p, y, n) in enumerate(sortPy):
#   if p in d:
#     d[p] += 1
#   else:
#     d[p] = 1
#   sortPy[i][2] = d[p]

# for p, y, n in py:
#   print(str(p).zfill(6) + str(n).zfill(6))
