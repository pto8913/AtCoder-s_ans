# URL: https://atcoder.jp/contests/abc096/tasks/abc096_c

H, W = map(int,input().split())
C = [input() for _ in range(H)]

ans = "Yes"
for i in range(H-1):
  for j in range(W-1):
    if(C[i][j] == "#"):
      if(i != 0 and C[i-1][j] == "#"):
        continue
      if(i != H and C[i+1][j] == "#"):
        continue
      if(j != 0 and C[i][j-1] == "#"):
        continue
      if(j != W and C[i][j+1] == "#"):
        continue
      ans = "No"
print(ans)
