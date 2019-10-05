import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
def main():
  n = ni()
  for _ in range(n):
    grade = ni()
    if grade < 36:
      print(grade)
    else:
      if grade % 10 == 5:
        print(grade)
      elif grade % 10 < 5:
        if (grade // 10) * 10 + 5 - grade < 3:
          print((grade // 10) * 10 + 5)
        else:
          print(grade)
      else:
        if (grade // 10 + 1) * 10 - grade < 3:
          print((grade // 10 + 1) * 10)
        else:
          print(grade)

main()