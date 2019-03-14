# URL: https://atcoder.jp/contests/abc067/tasks/arc078_a

N = int(input())
A = list(map(int,input().split()))

max_ = sum(A)
tmp = 0
ans = 1e9+10
for i in range(N-1):
  tmp += A[i]
  if(i+1 < N):
    ans = min(ans, abs(max_-2*tmp))
print(ans)
