import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    x = ni()

    print(x // 500 * 1000 + ((x - (x // 500) * 500) // 5) * 5)
    
if __name__ == '__main__':
    main()