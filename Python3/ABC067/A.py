# URL: https://atcoder.jp/contests/abc067/tasks/abc067_a

A, B = map(int,input().split())
if(A%3 == 0 or B%3 == 0 or (A+B)%3 == 0):
  print("Possible")
else:
  print("Impossible")
