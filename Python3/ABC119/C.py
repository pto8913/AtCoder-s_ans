# URL: https://atcoder.jp/contests/abc119/tasks/abc119_c
# DFS

N, A, B, C = map(int,input().split())
L = [int(input()) for _ in range(N)]

def dfs(x, a, b, c):
  if(x == N):
    if(min(a, b, c) > 0):
      return abs(a-A)+abs(b-B)+abs(c-C)-30
    else:
      return 1e9+7
  ret0 = dfs(x+1, a, b, c)
  ret1 = dfs(x+1, a+L[x], b, c) + 10
  ret2 = dfs(x+1, a, b+L[x], c) + 10
  ret3 = dfs(x+1, a, b, c+L[x]) + 10
  return min(ret0, ret1, ret2, ret3)
print(dfs(0, 0, 0, 0))
