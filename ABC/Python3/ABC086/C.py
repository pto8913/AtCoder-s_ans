# URL: https://atcoder.jp/contests/abc086/tasks/arc089_a

N = int(input())

ans = "Yes"
for _ in range(N):
  t, x, y = map(int,input().split())
  if((t+x+y)%2 == 1 or t < x+y):
    ans = "No"
    break
print(ans)
