import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))


def main():
    n = ni()
    a = na()
    a.sort()
    mid = n // 2
    if n % 2 == 0:
        y = sum(a[mid:])
        x = sum(a[:mid])
    else:
        y = sum(a[mid:])
        x = sum(a[:mid])
        
    print(y**2 + x**2)
main()