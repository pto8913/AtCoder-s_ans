# URL: https://atcoder.jp/contests/abc116/tasks/abc116_b

N = int(input())
memo = []
while True:
  if(N not in memo):
    memo.append(N)
  else:
    break
  if(N%2 == 0):
    N //= 2
  else:
    N = 3*N+1
print(len(memo)+1)
