import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    k, n = na()
    mid = k // 2
    a = na()

    ma = [] #minus
    pa = [] #pls
    for i in range(n - 1):
        x = a[i+1] - a[i]
        if x < 0:
            x = k - abs(x)
        ma.append(x)
    
    for i in range(n - 1, 0, -1):
        x = a[i] - a[i - 1]
        if x < 0:
            x = k - abs(x)
        pa.append(x)

    x = a[-1] - a[0]
    if x < 0:
        x = k - abs(x)
    ma.append(x)
    x = a[0] - a[-1]
    if x < 0:
        x = k - abs(x)
    pa.append(x)
    ma.sort()
    pa.sort()
    
    print(min(sum(ma[:-1]), sum(pa[:-1])))
if __name__ == '__main__':
    main()