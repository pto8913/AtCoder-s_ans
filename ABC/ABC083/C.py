# URL: https://atcoder.jp/contests/abc083/tasks/arc088_a

X, Y = map(int,input().split())

cnt = 0
while X <= Y:
  X = X*2
  cnt += 1
print(cnt)
