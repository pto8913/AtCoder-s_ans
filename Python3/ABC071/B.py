# URL: https://atcoder.jp/contests/abc071/tasks/abc071_b

S = input()
ans = "abcdefghijklmnopqrstuvwxyz"
for s in S:
  ans = ans.replace(s, "")
if(ans == ""):
  print("None")
else:
  print(ans[0])
