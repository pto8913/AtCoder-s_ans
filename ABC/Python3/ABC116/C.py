# URL: https://atcoder.jp/contests/abc116/tasks/abc116_c

N = int(input())
H = list(map(int,input().split()))
cnt = 0
for i in range(N-1):
  if(H[i] > H[i+1]):
    cnt += H[i] - H[i+1]
print(cnt+H[-1])
