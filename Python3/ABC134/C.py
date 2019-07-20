N = int(input())
A = [int(input()) for _ in range(N)]

m = [0, 0]
for i in range(N):
  if A[i] > m[0]:
    m[0] = A[i]
    m[1] = i  

m2 = 0
for i in range(N):
  if i == m[1]:
    continue
  m2 = max(A[i], m2)

res = []
for i in range(N):
  if i != m[1]:
    print(m[0])
  else:
    print(m2)
