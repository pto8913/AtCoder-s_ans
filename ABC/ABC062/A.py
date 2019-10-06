# URL: https://atcoder.jp/contests/abc062

x, y = map(int,input().split())

A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]
ans = "No"
if((x in A and y in A) or (x in B and y in B) or (x in C and y in C)):
  ans = "Yes"
print(ans)
