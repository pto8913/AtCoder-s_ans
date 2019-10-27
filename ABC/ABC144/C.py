import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def divi(n):
  res = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      res.append(i)
      if i != n // i:
        res.append(n // i)
  return res

def main():
  n = ni()

  x = divi(n)
  
  ans = 1e18+7
  for i in range(0, len(x), 2):
    # print(x[i])
    try:
      ans = min(ans, x[i] - 1 + x[i+1] - 1)
    except:
      ans = min(ans, (x[i] - 1) * 2)  
  print(ans)
  
main()