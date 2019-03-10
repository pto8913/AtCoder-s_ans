# URL: https://atcoder.jp/contests/abc105/tasks/abc105_b

N = int(input())
ans = "No"
for i in range(26):
  for j in range(16):
    if(i*4+j*7 == N):
      ans = "Yes"
print(ans)
