import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : map(int, stdin.readline().split())

def main():
  n = ni()

  odd = 1 if n%2 == 1 else 0
  for i in range(1, n+1):
    if i%2 == 0:
      odd += 1
  print(odd/n)

main()