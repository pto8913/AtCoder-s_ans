import sys

stdin = sys.stdin

sys.setrecursionlimit(10**6)

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))


def root(start, par, reach, c):
    reach.append(par)
    if start == c[par - 1]:
        return reach
    return root(start, c[par - 1], reach, c)

def main():
    q = ni()
    for _ in range(q):
        n = ni()
        a = na()
        ans = [0] * (n)
        for aa in a:
            reach = []
            res = root(aa, aa, reach, a)
            p = len(set(res))
            for r in res:
                ans[r - 1] = p
        print(*ans)

main()