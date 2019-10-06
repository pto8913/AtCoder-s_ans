# URL: https://atcoder.jp/contests/abc082/tasks/abc082_b

s = sorted(input())
t = sorted(input(), reverse = True)
ans = "No"
if(s < t):
  ans = "Yes"
print(ans)
