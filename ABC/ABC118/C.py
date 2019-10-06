# URL: https://atcoder.jp/contests/abc118/tasks/abc118_c

N = int(input())
A = list(map(int,input().split()))

def gcd(m, n):
  while n:
    m, n = n, m%n
  return m

def lcm(m, n):
  return (m*n)//gcd(m, n)
  
ans = A[0]
for i in range(1, N):
  ans = gcd(ans, A[i])
print(ans)
