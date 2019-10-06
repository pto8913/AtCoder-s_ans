# URL: https://atcoder.jp/contests/abc083/tasks/abc083_b

N, A, B = map(int,input().split())

cnt = 0
for i in range(1,N+1):
  if(A <= sum(map(int,str(i))) <= B):
    cnt += i
print(cnt)
