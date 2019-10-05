import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, m = na()
  if n % m == 0:
    print("egg")
  else:
    while n > 0:
      n -= m
    if n % 2 == 1:
      print("yopipa")
    else:
      print("egg")

main()