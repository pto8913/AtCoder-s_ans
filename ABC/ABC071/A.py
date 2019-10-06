# URL: https://atcoder.jp/contests/abc071/tasks/abc071_a

x, a, b = map(int,input().split())
ans = "A"
if(abs(x-a) > abs(x-b)):
  ans = "B"
print(ans)
