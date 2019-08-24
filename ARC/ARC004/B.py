import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  n = ni()
  d = []
  for _ in range(n):
    d.append(ni())
  mx = max(d)
  sm = sum(d)
  print(sm)
  if mx * 2 <= sm:
    print(0)
  else:
    print(mx - (sm - mx))

main()