N, M = map(int,input().split())
A = list(map(int,input().split()))
BC = [list(map(int,input().split())) for _ in range(M)]
BC.sort(key = lambda x: -x[1])

for B, C in BC:
  A.extend([C]*B)
  if len(A) > N*2:
    break
A.sort(reverse = True)
print(sum(A[:N]))
