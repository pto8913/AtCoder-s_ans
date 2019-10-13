import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  h, w = na()
  a = [ns() for _ in range(h)]
  a = ["".join(hw) for hw in zip(*a) if hw.count("#") > 0]
  a = ["".join(hw) for hw in zip(*a) if hw.count("#") > 0]
  print("\n".join(a))

main()