import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def gcd(n, m):
  while m:
    n, m = m, n%m
  return n

def main():
    a, b = na()

    print(a * b // gcd(a, b))

if __name__ == '__main__':
    main()