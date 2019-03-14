# URL: https://atcoder.jp/contests/abc065/tasks/arc076_a

A, B = map(int,input().split())
mod = 10**9+7
def factorical(n):
  ret = 1
  for i in range(1,n+1):
    ret *= i
    ret %= mod
  return ret%mod

a = factorical(A)
b = factorical(B)
if(abs(A-B) >= 2):
  print(0)
elif(A == B):
  print(a*b*2%mod)
else:
  print(a*b%mod)
