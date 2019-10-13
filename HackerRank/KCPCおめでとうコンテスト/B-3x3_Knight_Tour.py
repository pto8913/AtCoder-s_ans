import sys

stdin = sys.stdin

sys.setrecursionlimit(10**9)

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  s = []
  reach = [[True for _ in range(3)]for _ in range(3)]
  tmp = [[True for _ in range(3)]for _ in range(3)]
  for i in range(3):
    t = ns()
    for j, ss in enumerate(t):
      if ss == "0":
        reach[i][j] = False
    s.append(t)

  xx = [2, 2, -2, -2, 1, -1, 1, -1]
  yy = [1, -1, 1, -1, 2, 2, -2, -2]

  for y, sy in enumerate(s):
    cp = reach[:]
    for x, sx in enumerate(sy):
      if sx == "0":
        for i in range(8):
          yyy = y + yy[i]
          xxx = x + xx[i]
          if 0 <= yyy < 3 and 0 <= xxx < 3:
            if s[yyy][xxx] == "0":
              cp[yyy][xxx] = True
    if all(cp):
      print("Yes")
      # exit()
  print("No")

main()