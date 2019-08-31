import sys

stdin = sys.stdin
nl = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

def main():
  a, b = nl()
  n = ni()

  dame = []
  for _ in range(n):
    xx, yy = nl()
    dame.append((xx, yy))

  xy = [[0] * (a+2) for _ in range(b+2)]
  xy[1][1] = 1

  for y in range(1, b+1):
    for x in range(1, a+1):
      if (x+1, y) not in dame:
        xy[y][x+1] += xy[y][x]
      if (x, y+1) not in dame:
        xy[y+1][x] += xy[y][x]

  print(xy[b][a])

main()