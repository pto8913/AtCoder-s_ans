import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : map(int, stdin.readline().split())

def divi(n):
  res = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      res.append(i)
      if i != n // i:
        res.append(n // i)
  return res

def isprime(n):
  if n == 2:
    return True
  if n % 2 == 0 or n < 2:
    return False
  for i in range(3, int(n**0.5)+1, 2):
    if (n % i == 0):
      return False
  return True

def main():
  a, b = sorted(na())
  x = divi(a)
  cnt = 1
  for bb in divi(b):
    if bb in x and isprime(bb):
      cnt += 1
  print(cnt)
main()