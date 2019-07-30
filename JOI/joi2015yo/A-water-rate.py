A, B, C, D, P = [int(input()) for _ in range(5)]
if P < C:
  print(min(A*P, B))
else:
  print(min(A*P, (P-C)*D+B))