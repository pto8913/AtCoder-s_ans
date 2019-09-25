import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
na = lambda : map(int, stdin.readline().split())
ni = lambda : int(ns())
def main():
  n = ni()
  if n == 1:
    print(1)
    return
  nagasa = lambda x: len(str(x))
  def f(a, b):
    x = nagasa(a)
    y = nagasa(b)
    return x if x > y else y

  def divi(n):
    res = []
    for i in range(1, int(n**0.5)+1):
      if n % i == 0:
        res.append(i)
        if i != n // i:
          res.append(n // i)
    return res
  x = divi(n)
  ans = 1e9
  for a in x:
    b = n // a
    ans = min(ans, f(a, b))
  print(ans)

main()
