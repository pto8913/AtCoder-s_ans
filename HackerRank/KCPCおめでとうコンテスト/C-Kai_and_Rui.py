import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

mod = 998244353

def gcd(n, m):
  while m:
    n, m = m, n % m
  return n

def divi(n, c):
  res = {}
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      res[i] = c
      if i != n // i:
        res[n // i] = c
  return res

def factorial(n, b, div):
  res = 1
  for i in range(n, 1, -1):
    res *= i
    if i in div:
      div[i] -= 1
      res //= i
    res %= mod
  return res%mod, div

def f(n):
  res = 1
  for i in range(2, n):
    res *= i
  return res

def main():
  a, b, c = na()
  print(a % mod)
  # div = divi(b, c)
  # print(div)
  # print(factorial(a, b, div), b, c)
  # print(gcd(f(a), b**c))
main()