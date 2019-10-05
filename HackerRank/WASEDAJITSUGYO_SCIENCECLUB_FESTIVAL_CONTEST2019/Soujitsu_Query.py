import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  A = []
  q = ni()
  B = 0
  d = {}
  max_A = 0
  for _ in range(q):
    x = na()
    if len(x) == 1:
      if len(A) > 1:
        print(B * d[B])
    else:
      a, b = x
      if b in d:
        d[b] += 1
      else:
        d[b] = 1
      if A == []:
        A.append(b)
        max_A = b
        B = b
      else:
        if max_A == B > b:
          B = b
        elif b > max_A == B:
          max_A = b
        elif max_A > b > B:
          B = b
        elif b > max_A > B:
          B = max_A
          max_A = b
        A.append(b)
main()