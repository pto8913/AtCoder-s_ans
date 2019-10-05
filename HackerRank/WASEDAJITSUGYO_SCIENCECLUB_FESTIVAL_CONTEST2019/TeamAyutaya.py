import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, x = na()
  ans = "No"
  if x >= n:
    ans = "Yes"
  print(ans)

main()