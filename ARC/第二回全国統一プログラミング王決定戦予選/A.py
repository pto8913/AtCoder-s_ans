import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  n = ni()
  res = set()
  for i in range(1, n // 2 + 1):
    a, b = n - i, i
    if a == b:
        continue
    if (a, b) not in res and (b, a) not in res:
      res.add((a, b))
  print(len(res))
  
if __name__ == '__main__':
  main()