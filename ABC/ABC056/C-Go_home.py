import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
na = lambda : map(int, stdin.readline().split())
ni = lambda : int(ns())
def main():
  n = ni()
  f = lambda x: (x * (x+1)) // 2
  for i in range(1, n+1):
    if (f(i) >= n):
      print(i)
      return
main()
