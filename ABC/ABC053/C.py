import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  ans = n // 11 * 2
  if 0 < n % 11 < 7:
    ans += 1
  elif n % 11 > 6:
    ans += 2
  print(ans)
main()