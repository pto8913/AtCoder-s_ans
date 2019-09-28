import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : map(int, stdin.readline().split())

def main():
  n, k = na()
  h = list(na())
  cnt = 0
  for hh in h:  
    if hh >= k:
      cnt += 1
  print(cnt)

main()