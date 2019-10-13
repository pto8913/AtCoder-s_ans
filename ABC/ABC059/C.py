import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

n = ni()
a = na()

tmp = 0
for e in a:
  if tmp + e