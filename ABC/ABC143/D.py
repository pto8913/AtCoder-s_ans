import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

from bisect import bisect_left

def main():
    n = ni()
    l = sorted(na())
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            t = l[i] + l[j]
            ind = bisect_left(l, t)
            ans += max(0, ind - j - 1)
    print(ans)

main()