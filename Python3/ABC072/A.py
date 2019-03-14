# URL: https://atcoder.jp/contests/abc072/tasks/abc072_a

x, t = map(int,input().split())
ans = 0
if(t < x):
  ans = x-t
print(ans)
