import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    m, d = na()
    n, s = na()

    if s == 1:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
  main()