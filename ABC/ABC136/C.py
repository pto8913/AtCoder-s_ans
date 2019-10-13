import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  a = na()

  for i in range(n - 1, 1, -1):
    if a[i] > a[i - 1]:
      continue
    if a[i] < a[i - 1]:
      if a[i] == a[i - 1] - 1:
        a[i - 1] -= 1
        continue
    if a[i] == a[i - 1]:
      continue
    print("No")
    return
  print("Yes")
main()