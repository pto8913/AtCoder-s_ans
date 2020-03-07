import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def isprime(n):
  if n == 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if (n % i == 0):
      return False
  return True

def main():
    x = ni()

    for i in range(x, 2*10**5):
        if isprime(i) == True:
            print(i)
            return


if __name__ == '__main__':
    main()