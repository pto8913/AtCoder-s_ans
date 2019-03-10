# URL: https://atcoder.jp/contests/abc094/tasks/abc094_b

from bisect import bisect_left

N, M, X = map(int,input().split())
A = list(map(int,input().split()))
x = bisect_left(A, X)
print(min(x, M-x))
