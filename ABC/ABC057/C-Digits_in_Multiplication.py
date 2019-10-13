import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()

  def divi(n):
    res = []
    for i in range(1, int(n**0.5)+1):
      if n % i == 0:
        res.append(i)
        if i != n // i:
          res.append(n // i)
    return res

  def digitlen(n):
    return len(str(n))
  
  def f(a, b):
    x = digitlen(a)
    y = digitlen(b)
    if x >= y:
      return x
    else:
      return y

  if n == 1:
    print(1)
    return 

  ans = int(1e9+7)
  for e in divi(n):
    b = n // e
    ans = min(ans, f(e, b))
  print(ans)
  
main()