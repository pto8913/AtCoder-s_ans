import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

s = sn()

if s == "Sunny":
  print("Cloudy")
elif s == "Cloudy":
  print("Rainy")
elif s == "Rainy":
  print("Sunny")


