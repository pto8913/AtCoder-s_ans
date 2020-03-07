import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    a, b, k = na()

    newa = max(0, a - k)
    k = max(0, k - a)
    
    print(newa, max(0, b-k))

if __name__ == '__main__':
    main()