# URL: https://atcoder.jp/contests/abc109/tasks/abc109_c

N, X = map(int,input().split())
x = list(map(int,input().split()))

def gcd(m, n):
  while n:
    m, n = n, m%n
  return m

x = [abs(n-X) for n in x]
ans = x[0]
for i in range(1,N):
  ans = gcd(ans, x[i])
print(ans)
