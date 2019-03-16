# URL: https://atcoder.jp/contests/abc060/tasks/abc060_b

A, B, C = map(int,input().split())

ans = "NO"
for i in range(A,A*B+1,A):
  if(i%B == C):
    ans = "YES"
    break
print(ans)
