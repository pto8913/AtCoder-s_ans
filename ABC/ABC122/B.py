import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def check(In):
    return In != "A" and In != "C" and In != "G" and In != "T"

def main():
    s = ns()

    count = 0
    ans = 0
    for i in range(len(s)):
        if check(s[i]):
            count = 0
        else:
            count += 1
            ans = max(ans, count)
    print(ans)

if __name__ == '__main__':
    main()