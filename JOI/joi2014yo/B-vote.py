N, M = map(int,input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

competition = [0]*(N+1)
for b in B:
  for i, a in enumerate(A):
    if a <= b:
      i,a,b
      competition[i] += 1
      break
print(competition.index(max(competition))+1)

"""
N, M = map(int,input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

X = [0]*(N+1)
for b in B:
  t = [a for a in A if a <= b]
  X[t[0]] += 1
print(A.index(X.index(max(X)))+1)
"""