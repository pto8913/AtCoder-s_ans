# URL: https://atcoder.jp/contests/abc092/tasks/arc093_a

N = int(input())
A = [0]+list(map(int,input().split()))+[0]

maxMoney = sum([abs(A[i+1]-A[i]) for i in range(N+1)])
for i in range(1,N+1):
  print(maxMoney-abs(A[i-1]-A[i])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))
