import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  n = ni()
  s = ns()
  ans = ""
  for ss in s:
    x = ord(ss) + n
    if x > 90:
      x -= 26
    ans += chr(x)
  print(ans)

if __name__ == '__main__':
  main()