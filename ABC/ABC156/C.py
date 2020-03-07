import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  n, k = na()

  def Base_10_to_n(X, n):
    if (int(X/n)):
      return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
  
  print(len(Base_10_to_n(n, k)))

if __name__ == '__main__':
  main()