import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()

  mod = int(1e9+7)

  def divi(n):
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
      if n % i == 0:
        res += 1
        if i != n // i:
          res += 1
    return res

  def fact(n):
    res = 1
    for i in range(2, n + 1):
      res *= i
      res %= mod
    return res

  x = fact(n)

  print(divi(x % mod))

main()