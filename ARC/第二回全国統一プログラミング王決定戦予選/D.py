import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

import numpy as np

def comp(a, b):
  return min(a, b)

def main():
  n, m = na()  

  ar = [[0 for _ in range(n+1)]for _ in range(n+1)]
  for y in range(m):
    l, r, c = na()
    for x in range(l, r+1):
      ar[y][l:r+1] = 

if __name__ == '__main__':
  main()
