# URL: https://atcoder.jp/contests/abc111/tasks/arc103_a

from collections import Counter

N = int(input())
V = list(map(int,input().split()))
even = Counter(V[1::2]).most_common()+([[0, 0]])
odd = Counter(V[::2]).most_common()+([[0, 0]])
if(even[0][0] != odd[0][0]):
  print(N-even[0][1]-odd[0][1])
else:
  print(min(N-even[1][1]-odd[0][1], N-even[0][1]-odd[1][1]))

"""
collections.Counter

A = [1, 3, 4, 2, 1, 3, 5, 3]
c = collections.Counter(A)
print(c)
# Counter({3: 3, 1: 2, 4: 1, 2: 1, 5: 1})

print(c.most_common())
# [(3, 3), (1, 2), (4, 1), (2, 1), (5, 1)]

"""
