R, G, B, N = map(int,input().split())

cnt = 0
for i in range(N+1):
  for j in range(N+1):
    k = N - R*i - G*j
    if k >= 0:
      if k%B == 0:
        cnt += 1
    else:
      break
print(cnt)
