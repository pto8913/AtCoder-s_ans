# URL: https://atcoder.jp/contests/abc091/tasks/abc091_b

from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

s = Counter(S)
s[0] = 0
for t in T:
  if(t in s):
    s[t] -= 1
print(max(s.values()))
