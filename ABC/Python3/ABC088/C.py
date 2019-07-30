# URL: https://atcoder.jp/contests/abc088/tasks/abc088_c

C = [list(map(int,input().split())) for _ in range(3)]

b = [C[0][i]-0 for i in range(3)]
a = [C[i][0]-b[0] for i in range(3)]

ans = "Yes"
for i in range(3):
  for j in range(3):
    if(C[i][j] != a[i]+b[j]):
      ans = "No"
print(ans)
