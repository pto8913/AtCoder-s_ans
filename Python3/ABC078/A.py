# URL: https://atcoder.jp/contests/abc078/tasks/abc078_a

x, y = input().split()
ans = "="
if(x < y):
  ans = "<"
elif(x > y):
  ans = ">"
print(ans)
