import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, a, b = na()

  ans = 0
  for _ in range(n):
    s, d = ns().split()
    d = int(d)
    if d < a:
      if s == "East":
        ans += a
      else:
        ans -= a
    elif d > b:
      if s == "East":
        ans += b
      else:
        ans -= b
    else:
      if s == "East":
        ans += d
      else:
        ans -= d
    
  if ans == 0:
    print(0)
  elif ans < 0:
    print("West", -ans)
  else:
    print("East", ans)

main()