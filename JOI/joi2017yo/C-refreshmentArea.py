N, M, D = map(int,input().split())
C = [input() for _ in range(N)]
cnt = 0
for c in C:
  for i in range(M-D+1):
    if c[i:i+D] == "."*D:
      cnt += 1
for c in zip(*C):
  c = "".join(c)
  for i in range(N-D+1):
    if c[i:i+D] == "."*D:
      cnt += 1
print(cnt)