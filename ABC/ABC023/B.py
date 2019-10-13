import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  s = ns()

  ans = "b"
  for i in range(1, n + 1):
    if ans == s:
      print(i - 1)
      return
    if i % 3 == 1:
      ans = "a" + ans + "c"
    elif i % 3 == 2:
      ans = "c" + ans + "a"
    else:
      ans = "b" + ans + "b"
  print(-1)
main()