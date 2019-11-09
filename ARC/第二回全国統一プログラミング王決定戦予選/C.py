# I can't solve

import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  n = ni()
  a = na()
  b = na()

  biga = []
  smlb = []
  for i in range(n):
    if a[i] > b[i]:
      biga.append(a[i])
      smlb.append(b[i])
  
  ban = len(biga)

  if ban > n - 2:
    return "No"
  
  sa = sorted(biga)
  sb = sorted(smlb)
  print(sa)
  print(sb)
  for i in range(ban):
    if sa[i] > sb[i]:
      return "No"
  return "Yes"

if __name__ == '__main__':
  print(main())
