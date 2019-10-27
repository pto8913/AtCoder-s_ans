import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  a, b = na()
  if a > 9 or b > 9:
    print(-1)
    return
  print(a * b)

main()