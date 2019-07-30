# URL: https://atcoder.jp/contests/arc004/tasks/arc004_1

N = int(input())
XY = [[int(i) for i in input().split()]for _ in range(N)]
res = 0
for i in range(N):
  for j in range(i+1, N):
    x, y = XY[i][0], XY[i][1]
    x1, y1 = XY[j][0], XY[j][1]
    res = max(res, ((x1-x)**2+(y1-y)**2)**0.5)
print(res)
