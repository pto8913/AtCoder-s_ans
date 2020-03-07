import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : stdin.readline().split()
sys.setrecursionlimit(10 ** 7)

def main():
    s, t = na()
    print(t + s)


if __name__ == '__main__':
    main()