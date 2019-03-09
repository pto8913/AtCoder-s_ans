# URL: https://atcoder.jp/contests/abc119/tasks/abc119_b

N = int(input())
btc = 380000
money = 0
for _ in range(N):
  x, y = input().split()
  if(y == "BTC"):
    money += float(x)*btc
  else:
    money += int(x)
print(money)
