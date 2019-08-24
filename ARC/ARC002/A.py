import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  y = ni()

  uru = False
  if y % 400 == 0:
    uru = True
  elif y % 100 == 0:
    pass
  elif y % 4 == 0:
    uru = True

  if uru:
    print("YES")
  else:
    print("NO")

main()