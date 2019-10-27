import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
    N = ni()
    for _ in range(N):
        n = ni()
        p = na()
        m = ni()
        q = na()
        e = 0
        o = 0
        for pp in p:
            if pp % 2 == 0:
                e += 1
            else:
                o += 1
        e1 = 0
        o1 = 0
        for qq in q:
            if qq % 2 == 0:
                e1 += 1
            else:
                o1 += 1
        print(e * e1 + o * o1)         

main()
