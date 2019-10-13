import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  a, b = na()
  k = ni()
  p = na()

  x = [a, b]
  for pp in p:
    if pp in x:
      print("NO")
      return
    else:
      x.append(pp)
  print("YES")

main()