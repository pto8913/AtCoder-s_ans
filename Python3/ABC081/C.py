# URL: https://atcoder.jp/contests/abc081/tasks/arc086_a

from collections import Counter

N, K = map(int,input().split())
A = input().split()

a = Counter(A)
print(sum(sorted(a.values(), reverse = True)[K:]))
