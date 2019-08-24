import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

def f(n):
    return n*(n+1)//2

def main():
  n, k = an()
  a = list(an())

  mod = int(1e9)+7
  ans = 0
  x = a[:] 
  cnt = 0
  tcnt = 0
  for i, ai in enumerate(x):
    #cnt = 0
    for j in range(i+1, n):
      if ai > x[j]:
        cnt += 1
    #tcnt = 0
    for j in range(i+1):
      if ai > x[j]:
        tcnt += 1

  ans += f(k) * cnt
  ans %= mod
  ans += f(k - 1) * tcnt
  ans %= mod

  print(ans)

main()