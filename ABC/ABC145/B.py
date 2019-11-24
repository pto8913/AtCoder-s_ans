import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)


def main():
  n = ni()
  s = ns()
  mid = n // 2
#   print(s[0:mid], s[mid:n])
  if s[0:mid] == s[mid:n]:
    print("Yes")
  else:
    print("No")

if __name__ == '__main__':
  main()
