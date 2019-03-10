# URL: https://atcoder.jp/contests/abc117/tasks/abc117_b

N = int(input())
L = list(map(int,input().split()))
ans = "Yes"
for i in range(N):
  if(L[i] >= sum(L[:i]+L[i+1:])):
    ans = "No"
print(ans)
