N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

sortAB = sorted(AB, key = lambda x: (x[1]))
t = 0
for a, b in sortAB:
  t += a
  if t > b:
    print("No")
    break
else:
  print("Yes")
