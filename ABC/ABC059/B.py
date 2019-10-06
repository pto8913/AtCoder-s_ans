# URL: https://atcoder.jp/contests/abc059/tasks/abc059_b

a = int(input())
b = int(input())
ans = "EQUAL"
if(a > b):
  ans = "GREATER"
elif(a < b):
  ans = "LESS"
print(ans)
