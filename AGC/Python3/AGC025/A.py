# URL: https://atcoder.jp/contests/agc025/tasks/agc025_a

N = int(input())

def digSum(n):
  return sum(map(int, str(n)))

A = list(range(1,N//2+1))
B = list(range(N-1,N//2-1,-1))
ans = 1e9
for a, b in zip(A, B):
  ans = min(ans, digSum(a)+digSum(b))
print(ans)
