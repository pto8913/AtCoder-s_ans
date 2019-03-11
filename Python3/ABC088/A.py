# URL: https://atcoder.jp/contests/abc088/tasks/abc088_a

N = int(input())
A = int(input())

ans = "No"
if(N%500 <= A):
  ans = "Yes"
print(ans)
