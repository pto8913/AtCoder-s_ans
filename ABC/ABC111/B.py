# URL: https://atcoder.jp/contests/abc111/tasks/abc111_b

N = int(input())
if(N%111 == 0):
  print(N)
else:
  print((N//111+1)*111)
