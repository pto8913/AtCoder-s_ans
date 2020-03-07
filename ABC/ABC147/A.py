import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    a = na()

    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()