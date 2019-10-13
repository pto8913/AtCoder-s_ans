import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  t = 0
  for i in range(1, n + 1):
    t += i
    if t >= n:
      print(i)
      return
main()