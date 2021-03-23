import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  S = ns()
  n = len(S) - 1

  ans = 0
  for i in range(1 << n):
    tmp = S[0]
    for j in range(n):
      if (i >> j) & 1 == 1:
        tmp += "+"
      tmp += S[j+1]
    ans += eval(tmp)
  print(ans)

if __name__ == '__main__':
  main()