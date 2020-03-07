import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    s = ns()
    n = len(s)
    
    cnt = 0
    for i in range(n//2):
        # print(s[i],s[-i-1])
        if s[i] != s[-i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()