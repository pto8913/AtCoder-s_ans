S = input()
N = int(input())
A = [input() for _ in range(N)]
cnt = 0
for a in A:
  for i in range(len(a)):
    if S in a[i:]+a[:i]:
      cnt += 1
      break
print(cnt)