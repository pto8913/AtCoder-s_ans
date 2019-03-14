# URL: https://atcoder.jp/contests/abc070/tasks/abc070_c

N = int(input())
T = [int(input()) for _ in range(N)]

def gcd(m, n):
  while n:
    m, n = n, m%n
  return m

def lcm(m, n):
  return (m * n) // gcd(m, n)

ans = T[0]
for i in range(1,N):
  ans = lcm(ans, T[i])
print(ans)
