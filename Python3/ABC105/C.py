# URL: https://atcoder.jp/contests/abc105/tasks/abc105_c

N = int(input())
ans = ""
while N != 0:
  if(N%2 == 0):
    ans += "0"
  else:
    ans += "1"
  N -= 1
  N //= -2
if(ans == ""):
  ans = "0"
print(ans[::-1])
