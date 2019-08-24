import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  e = an()
  b = ni()
  l = an()

  dif = []
  cnt = 0
  for ll in l:
    if ll in e:
      cnt += 1
    else:
      dif.append(ll)

  if cnt == 6:
    print(1)
  elif cnt == 5:
    if dif[0] == b:
      print(2)
    else:
      print(3)
  elif cnt == 4:
    print(4)
  elif cnt == 3:
    print(5)
  else:
    print(0)

main()