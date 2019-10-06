# URL: https://atcoder.jp/contests/abc101/tasks/abc101_b

N = int(input())
if(N%sum(list(map(int,str(N)))) == 0):
  print("Yes")
else:
  print("No")
