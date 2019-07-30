H, W = map(int,input().split())
C = [input() for _ in range(H)]

cloud = [[0 if C[i][j] == "c" else -1 for j in range(W)] for i in range(H)]
for c in cloud:
  bottomCloud = False
  for i, cc in enumerate(c):
    if cc == 0:
      bottomCloud = True
    elif bottomCloud:
      c[i] = c[i-1]+1
      
for c in cloud:
  print(*c)