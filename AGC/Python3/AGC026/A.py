# URL: https://atcoder.jp/contests/agc026/tasks/agc026_a

from itertools import groupby

N = int(input())
A = list(map(int,input().split()))

ans = 0
for k, v in groupby(A):
  x = len(list(v))
  ans += x//2
print(ans)
