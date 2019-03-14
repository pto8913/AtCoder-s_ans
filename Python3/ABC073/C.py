# URL: https://atcoder.jp/contests/abc073/tasks/abc073_c

from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

a = Counter(A)
res = 0
for v in a.values():
  if(v%2 == 1):
    res += 1
print(res)
