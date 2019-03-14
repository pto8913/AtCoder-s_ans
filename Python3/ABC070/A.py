# URL: https://atcoder.jp/contests/abc070/tasks/abc070_a

N = input()
ans = "No"
if(N == N[::-1]):
  ans = "Yes"
print(ans)
