# abc58 c-怪文書.py

import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
na = lambda : map(int, stdin.readline().split())
ni = lambda : int(ns())
def main():
  n = ni()

  def indict(a, k):
    if k in a:
      a[k] += 1
    else:
      a[k] = 1

  def indict0(a, k, v):
    if k in a:
      a[k] = min(v, a[k])
    else:
      a[k] = v

  res = {}
  allin = {}
  d = {}
  for _ in range(n):
    s = ns()
    for e in s:
      indict(d, e)
    for k, v in d.items():
      indict(allin, k)
      indict0(res, k, v)
    res
    d = {}

  ans = ""
  for k, v in allin.items():
    if v != n:
      continue
    ans += res[k] * k
  print("".join(sorted(ans)))
main()
