import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
    n = ni()
    s = ns()

    res = s[0]
    pre = s[0]
    for i, ss in enumerate(s[1:]):
        if ss == pre:
            pass
        else:
            res += pre
            pre = ss
    if not res:
        print(1)
        return
    print(len(res))
main()