# URL: https://atcoder.jp/contests/abc075/tasks/abc075_b
# あまりよくないが確実

H, W = map(int,input().split())
S = [input() for _ in range(H)]
reach = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
  for j in range(W):
    if(S[i][j] == "#"):
      reach[i][j] = "#"
      if(reach[i-1][j-1] != "#"):
        reach[i-1][j-1] += 1
      if(reach[i-1][j] != "#"):
        reach[i-1][j] += 1
      if(reach[i-1][j+1] != "#"):
        reach[i-1][j+1] += 1
      if(reach[i][j-1] != "#"):
        reach[i][j-1] += 1
      if(reach[i][j+1] != "#"):
        reach[i][j+1] += 1
      if(reach[i+1][j-1] != "#"):
        reach[i+1][j-1] += 1
      if(reach[i+1][j] != "#"):
        reach[i+1][j] += 1
      if(reach[i+1][j+1] != "#"):
        reach[i+1][j+1] += 1
        
for r in reach[:-1]:
  print("".join(list(map(str, r[:W]))))
