import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
def main():
  s = ns()
  t = ns()

  cnt = 0
  for ss, tt in zip(s, t):
    if ss == tt:
      cnt += 1

  print(cnt)

main()

