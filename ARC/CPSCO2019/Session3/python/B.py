N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse = True)

cnt = 0
for a in A:
  if M <= 0:
    break
  M -= a
  cnt += 1
print(cnt)
