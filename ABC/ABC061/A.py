# URL: https://atcoder.jp/contests/abc061/tasks/abc061_a

a, b, c = map(int,input().split())
ans = "No"
if(a <= c <= b):
  ans = "Yes"
print(ans)
