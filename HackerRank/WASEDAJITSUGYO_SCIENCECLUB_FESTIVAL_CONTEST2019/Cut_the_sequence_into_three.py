import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def isOk(l, r):
  if l < 0 and r > 0:
    return False
  return True

def main():
  n = ni()
  a = na()

  wa = [0] * (n + 1)
  for i in range(n):
    wa[i + 1] = wa[i] + a[i]

  ans = int(1e18)
  for l in range(1, n - 1):
    lo = l
    hi = n - 1
    while lo + 1 != hi:
      mid = (lo + hi) // 2
      rl = wa[hi] - wa[l]
      rr = wa[-1] - wa[hi]
      ans = min(ans, max(wa[l], rr, rl) - min(wa[l], rr, rl))
      if rr > 0:
        hi = mid
      else:
        break
    # print(wa[l], rr, rl)
    rl = wa[hi] - wa[l]
    rr = wa[-1] - wa[hi]
    ans = min(ans, max(wa[l], rr, rl) - min(wa[l], rr, rl))
  print(ans)
main()