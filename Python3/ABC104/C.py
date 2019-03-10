# URL: https://atcoder.jp/contests/abc104/tasks/abc104_c
# 全探索

# bit全探索
D, G = map(int,input().split())
PC = [list(map(int,input().split())) for _ in range(D)]

ans = 1e9
for i in range(1 << D):
  point = 0
  cnt = 0
  for j in range(D):
    if(((i >> j) & 1) == 1):
      point += PC[j][0]*(j+1)*100 + PC[j][1]
      cnt += PC[j][0]
    else:
      tmp = j
  if(point < G):
    x = G - point
    if((PC[tmp][0]-1)*(tmp+1)*100 < x):
      continue
    cnt += -(-x//(100*(tmp+1)))
  ans = min(ans, cnt)
print(ans)

# DFS(深さ優先探索)
D, G = map(int,input().split())
PC = [0]+[list(map(int,input().split())) for _ in range(D)]

def dfs(d, g):
  if(d == 0):
    return 1e9

  x = min(g//(100*d), PC[d][0])
  point = x*100*d

  if(x == PC[d][0]):
    point += PC[d][1]
  
  if(point < g):
    x += dfs(d-1, g-point)
  
  return min(x, dfs(d-1, g))
print(dfs(D, G))
