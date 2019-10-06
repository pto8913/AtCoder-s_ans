N, L = map(int,input().split())

aji = [0]*N
for i in range(1,N+1):
  aji[i-1]=L+i-1

pi = sum(aji)
ans = 0
diff = []
for i in range(N):
  if pi - aji[i] == pi:
    print(pi)
    exit()
  diff.append(pi - aji[i])
if pi > 0:
  print(max(diff))
else:
  print(min(diff))
