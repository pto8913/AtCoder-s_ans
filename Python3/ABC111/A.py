# URL: https://atcoder.jp/contests/abc111/tasks/abc111_a

N = input()
ans = ""
for n in N:
  if(n == "1"):
    ans += "9"
  else:
    ans += "1"
print(ans)
