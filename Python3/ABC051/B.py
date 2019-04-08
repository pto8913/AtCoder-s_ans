# URL: https://atcoder.jp/contests/abc051/tasks/abc051_b

K, S = map(int,input().split())

cnt = 0
for i in range(K+1):
  for j in range(K+1):
    if 0 <= S-i-j < K+1:
      cnt += 1
print(cnt)
