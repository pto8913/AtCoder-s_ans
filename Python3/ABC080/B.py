# URL: https://atcoder.jp/contests/abc080/tasks/abc080_b

N = int(input())
ans = "No"
if(N%sum(map(int,str(N))) == 0):
  ans = "Yes"
print(ans)
