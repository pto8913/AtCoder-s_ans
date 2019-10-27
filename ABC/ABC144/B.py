import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  n = ni()

  for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            print("Yes")
            return
  print("No")

main()