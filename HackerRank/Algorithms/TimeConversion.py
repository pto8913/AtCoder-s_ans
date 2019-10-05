import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  s = ns()

  usiro = s[-2:]
  if usiro == "AM":
    hh = int(s[:2])
    if hh == 12:
      print("00" + s[2:-2])
    else:
      print(s[:-2])
  else:
    hh = int(s[:2])
    if hh == 12:
      print(s[:-2])
    else:
      print(str(hh + 12) + s[2:-2])
main()