import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  q = ni()
  while q:
    n = ni()
    m = 2 * n
    mat = [na() for _ in range(m)]

    ans = 0
    for y in range(n):
      for x in range(n):
        ans += max(mat[y][x], mat[y][m - 1 - x], mat[m - 1 - y][x], mat[m - 1 - y][m - 1 - x])
    print(ans)
    q -= 1

main()