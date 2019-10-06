# URL: https://atcoder.jp/contests/abc103/tasks/abc103_b

S = input()
T = input()

ans = "No"
for i in range(len(S)):
  if(S[i:]+S[:i] == T):
    ans = "Yes"
print(ans)
