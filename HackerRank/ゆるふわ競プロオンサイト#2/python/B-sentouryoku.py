def main():
  s = input()

  ata = lambda x: ord(x) - 64

  tasu = [ata(ss) for ss in s]
  n = len(s)
  ans = 1
  for i in range(n-1):
    x = tasu[i] + tasu[i+1]
    ans *= x
  print(ans)

main()
