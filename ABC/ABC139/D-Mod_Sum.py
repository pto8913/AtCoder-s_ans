import sys

stdin = sys.stdin
na = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

n = ni()

print(n*(n-1)//2)