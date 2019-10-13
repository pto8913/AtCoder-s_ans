import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  s = [ns() for _ in range(n)]
  ans = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      ans[j][n - i - 1] = s[i][j]
  for a in ans:
    print("".join(a))
main()