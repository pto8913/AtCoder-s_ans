N = int(input())
H = list(map(int,input().split()))

ans = 1
for i in range(1,N):
  cnt = 0
  for j in range(i):
    if i != j:
      if H[j] <= H[i]:
        cnt += 1
  if cnt == i:
    ans += 1
print(ans)
