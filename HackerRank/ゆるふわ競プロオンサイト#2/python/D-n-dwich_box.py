def main():
  import re

  s = input()
  res = []

  ptn = re.compile(r"(\|(#\|)*)")
  x = ptn.findall(s)
  for a, b in x:
    res.append(a.count("#") + 1)
  print(*res)

main()
