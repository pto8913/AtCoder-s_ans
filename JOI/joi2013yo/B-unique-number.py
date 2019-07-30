N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
A = [list(a) for a in zip(*A)]
player = [0]*N
for a in A:
  for i, aa in enumerate(a):
    if a.count(aa) == 1:
      player[i] += aa
print("\n".join(list(map(str,player))))

"""
N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
A = [list(a) for a in zip(*A)]
A = [[aa if a.count(aa) == 1 else 0 for aa in a]for a in A]
for a in zip(*A):
  print(sum(a))
"""