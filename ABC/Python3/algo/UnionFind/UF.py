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
    if(self.size(a) == self.size(b)):
      self.tree[a] -= 1
    self.tree[b] = a
  
  def size(self, a):
    return -self.tree[self.root(a)]

  def root(self, a):
    if(self.tree[a] < 0):
      return a
    else:
      res = self.root(self.tree[a])
      self.tree[a] = res
      return res

  def same(self, a, b):
    return self.root(a) == self.root(b)

N, Q = map(int,inp().split())
PAB = [list(map(int,input().split())) for _ in range(Q)]

uf = UnionFind(N)

ans = ["0", "1"]
for P, A, B in PAB:
  if(P == 0):
    uf.union(A, B)
  elif(P == 1):
    print(ans[uf.same(A, B)])
