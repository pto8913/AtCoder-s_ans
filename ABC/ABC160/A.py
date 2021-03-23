import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    s = ns()

    if s[2] == s[3] and s[4] == s[5]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()