import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n = ni()
  s = [ni() for _ in range(n)]
  s.sort()

  ans = sum(s)
  if ans % 10 == 0:
    change = False
    for e in s:
      if e % 10 != 0:
        ans -= e
        change = True
        break
    if change:
      print(ans)
    else:
      print(0)
  else:
    print(ans)

main()