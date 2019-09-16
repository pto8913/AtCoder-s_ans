import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())
def main():
  n, k, q = an()
  a = [ni() for _ in range(q)]

  point = [k] * n

  for aa in a:
    point[aa-1] += 1

  for p in point:
    p -= q
    if p <= 0:
      print("No")
    else:
      print("Yes")
main()
