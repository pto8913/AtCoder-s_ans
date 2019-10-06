import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  a = na()

  if n == 3:
    print(max(a) - min(a))
    return

  wa = [0] * (n + 1)
  for i in range(n):
    wa[i + 1] = wa[i] + a[i]

  ans = int(1e18+7)

  l = n // 2 - 1
  r = n // 2 + 1
  if n % 2 == 1:
    l += 1

  Q = wa[r] - wa[l]
  while l > 0 and r < n:
    P = wa[l] - wa[0]
    R = wa[-1] - wa[r]
    ans = min(max(P, Q, R) - min(P, Q, R), ans)
    if max(P, Q, R) == Q:
      if P > R:
        r += 1
      else:
        l -= 1
    else:
      if P > R:
        l -= 1
      elif P < R:
        r += 1
      else:
        lt, rt = l, r
        lc, rc = 1, 1
        while lt - lc > 0 and rt + rc < n:
          if wa[lt - lc] - wa[0] > wa[-1] - wa[rt + rc]:
            l -= lc
            r += rc
            break
          elif wa[lt - lc] - wa[0] < wa[-1] - wa[rt + rc]:
            r += rc
            l -= lc
            break
          else:
            lc -= 1
            rc += 1
    Q = wa[r] - wa[l]
  print(ans)
main()