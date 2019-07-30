import sys
sys.setrecursionlimit(10000000)

def dfs(x, y):
  if(x < 0 or x >= W or y < 0 or y >= H or maze[y][x] == "#"):
    return
  if(reach[y][x]):
    return False
  reach[y][x] = True
  if(maze[y][x] == "g"):
    return True
  return dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1)

H, W = map(int,input().split())
maze = [list(input()) for _ in range(H)]
reach = [[False]*W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if(maze[i][j] == "s"):
      s = [j, i]
if(dfs(s[0], s[1])):
  print("YES")
else:
  print("NO")
