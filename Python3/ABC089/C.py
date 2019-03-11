# URL: https://atcoder.jp/contests/abc089/tasks/abc089_c

from collections import Counter
from itertools import combinations
N = int(input())
S = Counter(input()[0] for _ in range(N))

ans = 0
for i, j, k in combinations("MARCH", 3):
  ans += S[i]*S[j]*S[k]
print(ans)
