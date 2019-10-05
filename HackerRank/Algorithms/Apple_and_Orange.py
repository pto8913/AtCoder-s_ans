import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  s, t = na()
  a, b = na()
  m, n = na()
  apple = na()
  orange = na()

  apl_cnt = 0
  for apl in apple:
    tmp = a + apl
    if s <= tmp <= t:
      apl_cnt += 1

  ora_cnt = 0
  for ora in orange:
    tmp = b + ora
    if s <= tmp <= t:
      ora_cnt += 1

  print(apl_cnt)
  print(ora_cnt)
main()