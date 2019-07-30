# URL: https://atcoder.jp/contests/abc093/tasks/arc094_a

A, B, C = sorted(map(int,input().split()))
x = C*2-A-B
if(x%2 == 0):
  print(x//2)
else:
  print((x+3)//2)
