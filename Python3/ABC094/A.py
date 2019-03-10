# URL: https://atcoder.jp/contests/abc094/tasks/abc094_a

A, B, X = map(int,input().split())
ans = "NO"
if(X <= A+B and A <= X):
  ans = "YES"
print(ans)
