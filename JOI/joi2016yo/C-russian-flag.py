from itertools import product

N, M = map(int,input().split())
F = [input() for _ in range(N)]

X = list(range(1,N-1))
ans = 1e9
for pro in product(X, repeat = 3):
  if sum(pro) == N:
    w, b, r = 0, 0, 0
    x, y, z = pro
    for i in range(x):
      w += M-F[i].count("W")
    for i in range(x, y+x):
      b += M-F[i].count("B")
    for i in range(y+x, y+x+z):
      r += M-F[i].count("R")
    ans = min(ans, w+b+r)
print(ans)