# URL: https://atcoder.jp/contests/abc097/tasks/abc097_b

X = int(input())

ans = 1
for i in range(1,X+1):
  for j in [2, 3, 5, 7]:
    if(i**j < X):
      ans = max(ans, i**j)
print(ans)
