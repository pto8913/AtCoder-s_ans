# URL: https://atcoder.jp/contests/abc102/tasks/abc102_a

N = int(input())

def gcd(m, n):
  while n:
    m, n = n, m%n
  return m

def lcm(m, n):
  return (m * n) // gcd(m, n)

print(lcm(2, N))
