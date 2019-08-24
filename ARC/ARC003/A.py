import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  n = ni()
  s = sn()

  a = s.count("A")
  b = s.count("B")
  c = s.count("C")
  d = s.count("D")
  print((a*4 + b*3 + c*2 + d) / n)

main()