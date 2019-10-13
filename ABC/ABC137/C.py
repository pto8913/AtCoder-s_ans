import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()

  d = {}
  for _ in range(n):
    s = "".join(sorted(ns()))
    if s in d:
      d[s] += 1
    else:
      d[s] = 1

  ans = 0
  for k, v in d.items():
    ans += (v * (v - 1)) // 2
  print(ans)

main()