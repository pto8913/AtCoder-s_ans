import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    n = ni()
    a = na()

    cur = 1
    cnt = 0
    is_ok = False
    for aa in a:
        if aa == cur:
            is_ok = True
            cur += 1
        else:
            cnt += 1
    if is_ok:
        print(cnt)
    else:
        print(-1)
if __name__ == '__main__':
    main()