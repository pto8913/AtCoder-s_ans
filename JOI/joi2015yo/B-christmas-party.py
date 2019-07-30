N = int(input())
M = int(input())
A = list(map(int,input().split()))
B = [[int(i) for i in input().split()]for _ in range(M)]

friends = [0]*N
for i, a in enumerate(A):
  for j, b in enumerate(B[i]):
    if a == b:
      friends[j] += 1
    else:
      friends[a-1] += 1
print("\n".join(list(map(str,friends))))