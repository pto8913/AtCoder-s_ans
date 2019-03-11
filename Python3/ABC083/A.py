# URL: https://atcoder.jp/contests/abc083/tasks/abc083_a

A, B, C, D = map(int,input().split())
l = A+B
r = C+D
if(l > r):
  print("Left")
elif(r > l):
  print("Right")
else:
  print("Balanced")
