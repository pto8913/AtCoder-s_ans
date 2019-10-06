# URL: https://atcoder.jp/contests/abc120/tasks/abc120_b

A, B, K = map(int,input().split())
tmp = []
for i in range(1,101):
  if(A%i == B%i == 0):
    tmp.append(i)
print(tmp[-K])
