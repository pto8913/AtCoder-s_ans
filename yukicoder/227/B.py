import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  a = na()

  q = ni()
  for _ in range(q):
    l, r = na()
    gcnt = 0
    lcnt = 0
    ecnt = 0
    for i in range(l, r):
      if a[i] <= a[i+1]:
        gcnt += 1
      if a[i] >= a[i+1]:
        lcnt += 1
      if a[i] == a[i+1]:
        ecnt += 1
    c = r - l
    if gcnt == c:
      if ecnt == c:
        print(1, 1)
        continue
      print(1, 0)
    if lcnt == c:
      if ecnt == c:
        print(1, 1)
        continue
      print(0, 1)
    if ecnt == c:
      print(1, 1)
    if gcnt != c and lcnt != c and ecnt != c:
      print(0, 0)

main()