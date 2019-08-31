import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

n = ni()

zahyo = []
for _ in range(n):
  zahyo.append(tuple(list(na())))

for x, y in zahyo:
  