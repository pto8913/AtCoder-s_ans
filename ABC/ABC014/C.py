import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, x = na()
  a = na()

  cnt = 0
  for i, b in enumerate(format(x, 'b')[::-1][:n]):
    if b == "1":
      cnt += a[i]
  print(cnt)
main()