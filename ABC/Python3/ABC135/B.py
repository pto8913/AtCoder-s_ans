N = int(input())
A = list(map(int,input().split()))

x = list(range(1,N+1))

cnt = 0
for i, a in enumerate(A):
  if a != x[i]:
    cnt += 1
if cnt <= 2:
  print("YES")
else:
  print("NO")
