import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

mod = 998244353
from collections import Counter

def main():
  n = ni()
  d = na()

  if d[0] != 0:
    print(0)
    return
  
  pre = 0
  for dd in set(d[1:]):
    if dd - pre > 1 or dd == 0:
      print(0)
      return
    pre = dd

  dic = {}
  for dd in d:
    if dd in dic:
      dic[dd] += 1
    else:
      dic[dd] = 1

  ans = 1
  t = sorted(dic.items(), key = lambda x: x[0])
  for i in range(1, len(t) - 1):
    x = (t[i][1] ** t[i+1][1]) % mod
    ans *= x
    ans %= mod
  print(ans % mod)
 

if __name__ == '__main__':
  main()