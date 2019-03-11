# URL: https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int,input().split())

for i in range(N+1):
  for j in range(N+1):
    k = N-i-j
    if(k >= 0):
      if(10000*i+5000*j+1000*k == Y):
        print(i,j,k)
        exit()
print(-1,-1,-1)
