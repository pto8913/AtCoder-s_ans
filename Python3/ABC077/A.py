# URL: https://atcoder.jp/contests/abc077/tasks/abc077_a

S = input()
T = input()
ans = "NO"
if(S[::-1] == T and S == T[::-1]):
  ans = "YES"
print(ans)
