# URL: https://atcoder.jp/contests/abc086/tasks/abc086_a

a, b = map(int,input().split())
ans = "Odd"
if(a*b%2 == 0):
  ans = "Even"
print(ans)
