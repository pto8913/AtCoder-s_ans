# URL: https://atcoder.jp/contests/abc084/tasks/abc084_b

A, B = map(int,input().split())
S = input()

ans = "No"
if(S[A] == "-"):
  if(S[:A].isdigit() and S[A+1:].isdigit()):
    ans = "Yes"
print(ans)

"""
isdigit

x = "123"
print(x.isdigit())
# True

x = "1b2"
print(x.isdigit())
# False
"""
