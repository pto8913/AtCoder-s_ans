A, B, C, D = map(int,input().split())

def gcd(m, n):
  while n:
    m, n = n, m%n
  return m

def lcm(m, n):
  return (m * n) // gcd(m, n)

def f(n, m, l):
  a = n // l
  if l * a < n:
    a += 1
  b = m // l
  return b - a + 1

N = B - A + 1
print(N - (f(A, B, C) + f(A, B, D) - f(A, B, lcm(C, D))))
