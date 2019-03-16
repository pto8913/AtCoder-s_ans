# URL: https://atcoder.jp/contests/abc060/tasks/arc073_a

N, T = map(int,input().split())
t = list(map(int,input().split()))

cnt = T
for i in range(N-1):
  cnt += min(T, t[i+1]-t[i])
print(cnt)
