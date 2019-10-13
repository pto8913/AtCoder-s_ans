import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, q = na()
  s = ns()
  x = []
  for ss in s:
    if ss == "*":
      x.append(1)
    else:
      x.append(0)

  wa = [0] * (n + 1)
  for i in range(n):
    if x[i - 1] >= x[i]:
      wa[i + 1] = wa[i]
      continue
    if x[i - 1] < x[i]:
      wa[i + 1] = wa[i] + x[i]

  for _ in range(q):
    a, b = na()
    print(wa[b - 1] - wa[a - 1])

main()