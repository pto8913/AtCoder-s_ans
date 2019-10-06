# URL: https://atcoder.jp/contests/abc060/tasks/abc060_a

A, B, C = input().split()
ans = "NO"
if A[-1] == B[0] and B[-1] == C[0]:
  ans = "YES"
print(ans)
