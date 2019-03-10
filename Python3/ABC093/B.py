# URL: https://atcoder.jp/contests/abc093/tasks/abc093_b

A, B, K = map(int,input().split())
x = set()
for i in range(A, B+1)[:K]:
  x.add(i)
for i in range(A, B+1)[-K:]:
  x.add(i)
for xx in sorted(x):
  print(xx)
