N, K = map(int,input().split())

def check(n):
  cnt = 0
  while n < K:
    n *= 2
    cnt += 1
  return cnt

point = 0
x = 1 / N
y = 1 / 2
for i in range(1, N+1):
  res = check(i)
  point += x * (y**res)
print(point)
