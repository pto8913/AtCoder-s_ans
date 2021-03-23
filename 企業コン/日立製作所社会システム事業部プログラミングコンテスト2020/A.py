import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    s = ns()

    n = len(s)
    if n % 2 == 1:
        print("No")
    else:
        tmp = ""
        for i in range(n//2):
            tmp += "hi"
        if s == tmp:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()