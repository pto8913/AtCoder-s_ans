import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()

  def f(n):
    while n - 4 >= 0:
      n -= 4
      if n % 3 == 0:
        return n
    return n
  
  def f0(n):
    while n - 3 >= 0:
      n -= 3
      if n % 4 == 0:
        return n
    return n
  
  tmp = n
  tmp = f(tmp)
  if tmp == 0 or tmp % 3 == 0:
    return 1
  tmp = f0(tmp)
  if tmp == 0 or tmp % 4 == 0:
    return 1

  tmp = n
  tmp = f0(tmp)
  if tmp == 0 or tmp % 4 == 0:
    return 1
  tmp = f(tmp)
  if tmp == 0 or tmp % 3 == 0:
    return 1
  return 0
  
print("Yes" if main() else "No")