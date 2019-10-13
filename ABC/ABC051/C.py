import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  sx, sy, tx, ty = na()

  ans = ""
  y = ty - sy
  x = tx - sx
  ans += y * "U"
  ans += x * "R"
  ans += y * "D"
  ans += x * "L"
  ans += "L"
  ans += (y + 1) * "U"
  ans += (x + 1) * "R"
  ans += "DR"
  ans += (y + 1) * "D"
  ans += (x + 1) * "L"
  ans += "U"
  print(ans)

main()