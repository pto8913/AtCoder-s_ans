import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

def main():
  a, b = na()
  
  tmp = 1
  cnt = 0
  while tmp < b:
    tmp += a-1
    cnt += 1
  print(cnt)

main()