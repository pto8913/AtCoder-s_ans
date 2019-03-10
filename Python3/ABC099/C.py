# URL: https://atcoder.jp/contests/abc099/tasks/abc099_c

# 遅い
N = int(input())

ans = 1e9
for i in range(N+1):
  cnt = 0
  tmp = i
  while tmp > 0:
    cnt += tmp%6
    tmp //= 6
  tmp = N-i
  while tmp > 0:
    cnt += tmp%9
    tmp //= 9
  ans = min(ans, cnt)
print(ans)

# DFS
# 早い
from itertools import count, takewhile
N = int(input())

def dfs(n, d={}):
  if(n <= 6):
    return n
  if(n in d):
    return d[n]
  mn = max(takewhile(lambda x: x<=n, (9**i for i in count())))
  ms = max(takewhile(lambda x: x<=n, (6**i for i in count())))
  d[n] = min(dfs(n-mn), dfs(n-ms))+1
  return d[n]

print(dfs(N))

# DP
# とても遅い
N = int(input())
x = 10**5+1
dp = [0]*x
L = [1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]
for i in range(x):
  for j in range(len(L)):
    if(1 <= i+L[j] <= x-1):
      if(dp[i+L[j]] == 0):
        dp[i+L[j]] = dp[i]+1
      else:
        dp[i+L[j]] = min(dp[i]+1, dp[i+L[j]])
print(dp[N])
