# URL: https://atcoder.jp/contests/abc079/tasks/abc079_a

N = input()
ans = "No"
if(N[0] == N[1] == N[2] or N[1] == N[2] == N[3]):
  ans = "Yes"
print(ans)
