N = int(input())
A = list(map(int,input().split()))

cnt = 0
res = 0
for i in range(N):
  if A[i] == 1:
    cnt += 1
  else:
    res = max(res, cnt)
    cnt = 0
res = max(res, cnt)
print(res+1)

"""
N = int(input())
A = list(map(int,input().split()))+[0]

cnt = 0
res = 0
for a in A:
  if a == 1:
    cnt += 1
  else:
    res = max(res, cnt+1)
    cnt = 0
print(res)
"""