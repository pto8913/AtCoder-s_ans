import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

"""def main():
  n = ni()
  a = na()

  if n == 3:
    print(max(a) - min(a))
    return

  wa = [0] * (n + 1)
  for i in range(n):
    wa[i+1] = wa[i] + a[i]
  
  mae = {}
  for s in range(1, n):
    mae[s] = wa[s] - wa[0]

  ans = int(1e9 + 7)
  for t in range(n, 1, -1):
    P = mae[n - t + 1]
    R = wa[-1] - wa[t]
    Q = wa[-1] - P - R
    ans = min(max(P, Q, R) - min(P, Q, R), ans)
  print(ans)

main()"""