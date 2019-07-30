# URL: https://atcoder.jp/contests/agc032/tasks/agc032_a

N = int(input())
B = list(map(int,input().split()))

A = []
for i in range(1,N+1):
  if(B == []):
    break
  for b in B:
    if(1 <= b <= i):
      A.insert(b-1, b)
      B.remove(b)
    break

if(B == []):
  for a in A:
    print(a)
  exit()
print(-1)
