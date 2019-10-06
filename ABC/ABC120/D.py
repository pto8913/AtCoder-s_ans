# URL: https://atcoder.jp/contests/abc120/tasks/abc120_d
# UnionFind

class UnionFind:
  def __init__(self, n):
    self.tree = [-1] * n
  
  def union(self, a, b):
    a = self.root(a)
    b = self.root(b)
    if(a == b):
      return
    if(self.size(a) < self.size(b)):
      a, b = b, a
    self.tree[a] += self.tree[b]
    self.tree[b] = a
    
  def root(self, a):
    if(self.tree[a] < 0):
      return a
    res = self.root(self.tree[a])
    self.tree[a] = res
    return res
    
  def size(self, a):
    return -self.tree[self.root(a)]

N, M = map(int,input().split())
A, B = [], []
for _ in range(M):
  a, b = map(int,input().split())
  A.append(a-1)
  B.append(b-1)

uf = UnionFind(N)

res = N*(N-1)//2
result = [0] * M
for i in range(M-1, -1, -1):
  result[i] = res
  if(uf.root(A[i]) != uf.root(B[i])):
    res -= uf.size(A[i]) * uf.size(B[i])
    uf.union(A[i], B[i])

for r in result:
  print(r)
