# URL: https://atcoder.jp/contests/abc092/tasks/abc092_b

N = int(input())
D, X = map(int,input().split())
A = [int(input()) for _ in range(N)]
ans = X
for a in A:
  day = 1
  while a <= D:
    day += a
    ans += 1
print(ans)
