import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  a, b, x = na()

  ans = 0
  s = []
  for i in range(1, 11):
    n = (x - b * i) // a
    w = a * n + i * b
    if w <= x and n > 0:
      s.append(n)
  
  for ss in s:
    ss = min(ss, int(1e9))
    t = a * ss + len(str(ss)) * b
    ts = ss + 1
    if ts >= int(1e9):
      ts = int(1e9)
    tt = a * ts + len(str(ts)) * b
    if t <= x or tt <= x:
      ans = max(ans, ss)
  
  return ans

if __name__ == '__main__':
  print(main())
