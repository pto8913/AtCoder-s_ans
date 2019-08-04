def main():
  N = int(input())
  H = list(map(int,input().split()))

  ma = H[-1]
  ans = "Yes"
  for i, h in enumerate(H[::-1]):
    if i == 0:
      continue
    if ma > h:
      ma = h
      continue
    if ma < h:
      if ma + 1 == h:
        continue
      ans = "No"
    if ma == h:
      continue
  print(ans)

if __name__ == "__main__":
  main()
