# URL: https://atcoder.jp/contests/abc066/tasks/arc077_a

N = int(input())
A = input().split()

if(N%2 == 0):
  print(*(A[::-2]+A[::2]))
else:
  print(*(A[::-2]+A[1::2]))
