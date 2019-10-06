import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : map(int, stdin.readline().split())

def main():
  n = ni()
  a = list(na())
  d = {}
  for i, a in enumerate(a):
    d[a] = i+1
  res = []
  for i in range(n):
    res.append(d[i+1])
  print(*res)

main()