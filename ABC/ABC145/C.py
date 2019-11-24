import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

from math import factorial
from itertools import permutations

def main():
  n = ni()
  xy = [na() for _ in range(n)]

  ff = lambda a, b, c, d: ((a - b) ** 2 + (c - d) ** 2) ** 0.5

  res = []
  for per in permutations(range(n)):
    tmp = 0
    for i, pp in enumerate(per[:-1]):
      tmp += ff(xy[pp][0], xy[per[i+1]][0], xy[pp][1], xy[per[i+1]][1])
    res.append(tmp)
  print(sum(res) / factorial(n))


if __name__ == '__main__':
  main()
 
