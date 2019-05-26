N = int(input())
SP = [input().split() for _ in range(N)]
r = []
g= 1
for x, y in SP:
  r.append([x, int(y), g])
  g+=1

sortV = sorted(r, key = lambda x: -x[1])
sortK = sorted(sortV, key = lambda x: x[0])

for x, y,z in sortK:
  print(z)
