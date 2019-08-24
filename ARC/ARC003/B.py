import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  n = ni()
  s = []
  for _ in range(n):
    s.append(sn())

  sortS = []
  for ss in s:
    sortS.append(ss[::-1])
  sortS.sort()

  for e in sortS:
    print(e[::-1])

main()