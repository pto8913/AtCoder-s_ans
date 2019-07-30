# URL: https://atcoder.jp/contests/abc110/tasks/abc110_b

N, M, X, Y = map(int,input().split())
x = sorted(list(map(int,input().split())))
y = sorted(list(map(int,input().split())))
ans = "War"
for i in range(X+1,Y+1):
  if(x[-1] < i <= y[0]):
    ans = "No War"
print(ans)
