import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

MAX = int(1e9+7)

def main():
  n = ni()
  h = list(na()) + [MAX]

  cnt = 0
  check = 0
  tmp = []
  for i in range(n):
    hh = h[i]
    if not check:
      check = hh
    if check >= h[i+1]:
      cnt += 1
      check = h[i+1]
    else:
      tmp.append(cnt)
      check = 0
      cnt = 0

  print(max(tmp))

main()