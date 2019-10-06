# URL: https://atcoder.jp/contests/abc086/tasks/abc086_b

a, b = input().split()
x = int(a+b)**0.5
ans = "No"
if(x == int(x)):
  ans = "Yes"
print(ans)
