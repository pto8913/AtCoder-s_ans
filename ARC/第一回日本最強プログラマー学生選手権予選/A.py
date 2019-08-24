import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())
def main():
  m, d = an()

  cnt = 0
  for mm in range(1, m+1):
    for i in range(10, d+1):
      d1, d2 = str(i)
      d1 = int(d1)
      d2 = int(d2)
      if d1 >= 2 and d2 >= 2 and d1 * d2 == mm:
        cnt += 1
  print(cnt)

main()