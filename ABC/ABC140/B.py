import sys

stdin = sys.stdin.readline
na = lambda: map(int, stdin().split())
ns = lambda: stdin().rstrip()
ni = lambda: int(ns())
def main():
  n = ni()
  a = list(na())
  b = list(na())
  c = list(na())

  ans = 0
  pre = 0
  for i, aa in enumerate(a):
    aa -= 1
    if i >= 1 and i <= n-1 and pre+1 == aa:
      ans += c[aa-1]
    ans += b[aa]
    pre = aa
  print(ans)
main()