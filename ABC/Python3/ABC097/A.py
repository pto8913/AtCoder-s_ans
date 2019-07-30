# URL: https://atcoder.jp/contests/abc097/tasks/abc097_a

a, b, c, d = map(int,input().split())
ans = "No"
if((abs(b-a) <= d and abs(c-b) <= d) or abs(c-a) <= d):
  ans = "Yes"
print(ans)
