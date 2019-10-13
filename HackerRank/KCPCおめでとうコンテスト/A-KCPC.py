import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

s = ns()
if s == "KCPC":
  print("Yes")
elif s == "KUPC":
  print("Yes?")
else:
  print("No")