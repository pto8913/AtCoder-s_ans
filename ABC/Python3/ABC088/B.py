# URL: https://atcoder.jp/contests/abc088/tasks/abc088_b

N = int(input())
A = sorted(list(map(int,input().split())), reverse = True)

a = 0
b = 0
for i in range(0,N,2):
  a += A[i]
for i in range(1,N,2):
  b += A[i]
print(a-b)
