# URL: https://atcoder.jp/contests/abc068/tasks/arc079_a

N, M = map(int,input().split())

e = [0]*N
for _ in range(M):
  a, b = map(int,input().split())
  if(a == 1):
    e[b] += 1
  elif(b == N):
    e[a] += 1
if(2 in e):
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
