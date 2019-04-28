N = int(input())
A = list(map(int,input().split()))

neg_cnt = 0
for a in A:
  if a < 0:
    neg_cnt += 1

B = list(map(abs, A))
if neg_cnt%2 == 0:
  print(sum(B))
else:
  print(sum(B) - 2*min(B))
