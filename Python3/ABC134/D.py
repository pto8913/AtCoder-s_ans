N = int(input())
A = list(map(int,input().split()))
box = [0] * (N+1)
res = []

for i in range(1, N+1)[::-1]:
  s = 0
  for j in range(1, N // i):
    s += box[(j+1)*i]
  if s % 2 != A[i-1]:
    box[i] = 1
    res.append(i)

print(len(res))
print(*res)
