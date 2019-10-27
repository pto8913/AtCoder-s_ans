import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
    n = ni()
    d = na()

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    
    print(ans)

main()