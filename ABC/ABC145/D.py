import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def mod_combination(n, k, mod = 10 ** 9 + 7):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)
    p, q = 1, 1
    for i in range(n - k + 1, n + 1):
        p = (p * i) % mod
    for i in range(2, k + 1):
        q = (q * i) % mod
    return p * (extended_gcd(q, mod)[1] % mod) % mod

def main():
  x, y = na()
  if (x + y) % 3 != 0 or x * 2 < y or y * 2 < x:
    print(0)
    return
  n = (x + y) // 3
  print(mod_combination(n, y - n))
 

if __name__ == '__main__':
  main()
