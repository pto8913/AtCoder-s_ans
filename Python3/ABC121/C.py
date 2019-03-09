# URL: https://atcoder.jp/contests/abc121/tasks/abc121_c

N, M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB = sorted(AB, key = lambda x: x[0])
money = 0
for a, b in AB:
  if(M < 0):
    break
  if(b <= M):
    money += a*b
  else:
    money += M*a
  M -= b
print(money)
