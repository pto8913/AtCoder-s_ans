import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  s = ns()

  if s == "SUN":
    print(7)
  elif s == "MON":
    print(6)
  elif s == "TUE":
    print(5)
  elif s == "WED":
    print(4)
  elif s == "THU":
    print(3)
  elif s == "FRI":
    print(2)
  elif s == "SAT":
    print(1)

if __name__ == '__main__':
  main()