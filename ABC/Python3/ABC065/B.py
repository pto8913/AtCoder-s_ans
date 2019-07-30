# URL: https://atcoder.jp/contests/abc065/tasks/abc065_b

N = int(input())
A = [int(input()) for _ in range(N)]

b = 0
for i in range(N):
  if(b != 0):
    b -= 1
  b = A[b]
  if(b == 2):
    print(i+1)
    break
else:
  print(-1)
