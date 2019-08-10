def main():
  N = int(input())
  S = [input() for _ in range(N)]

  d = {}
  for i, s in enumerate(S):
    x = "".join(sorted(s))
    if x in d:
      d[x] += 1
    else:
      d[x] = 1
  
  cnt = 0
  for v in d.values():
    if v == 1:
      continue
    if v == 2:
      cnt += 1
    elif v == 3:
      cnt += v
    else:
      cnt += sum(list(range(1,v)))

  print(cnt)
if __name__ == "__main__":
  main()
