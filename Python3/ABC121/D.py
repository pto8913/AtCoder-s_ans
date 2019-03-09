# URL: https://atcoder.jp/contests/abc121/tasks/abc121_d

import sys
inp = sys.stdin.readline
A, B = map(int,inp().split())

def f(x):
  if(x%4 == 0):
    return x
  elif(x%4 == 1):
    return x^(x-1)
  elif(x%4 == 2):
    return x^(x-1)^(x-2)
  elif(x%4 == 3):
    return 0
print(f(B) ^ f(A-1))
