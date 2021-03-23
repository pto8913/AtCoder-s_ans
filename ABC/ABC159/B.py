import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    s = ns()
    n = len(s)
    mid = s[:(n - 1) // 2]
    san = s[(n + 3) // 2 - 1:]
    
    if s == s[::-1]:
        if mid == mid[::-1]:
            if san == san[::-1]:
                print("Yes")
                return
    print("No")    


if __name__ == '__main__':
    main()