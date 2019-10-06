import sys

stdin = sys.stdin.readline
na = lambda: map(int, stdin().split())
ns = lambda: stdin().rstrip()
ni = lambda: int(ns())

n = ni()
print(n**3)