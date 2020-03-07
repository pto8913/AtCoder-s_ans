import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    n, k = na()
    r, s, p = na()
    t = ns()

    ans = 0
    for i, tt in enumerate(t):
        

if __name__ == '__main__':
    main()