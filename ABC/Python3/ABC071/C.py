# URL: https://atcoder.jp/contests/abc071/tasks/arc081_a

from collections import Counter

N = int(input())
A = list(map(int,input().split()))

a = Counter(A)

x, y = 0, 0
for k, v in a.items():
  if(v >= 2 and k > y):
    if(k >= x):
      if(v >= 4):
        y = k
      else:
        y = x
      x = k
    else:
      y = k
print(x*y)
