import sys

stdin = sys.stdin
nl = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())
def main():
  n, k = nl()

  kaidan = [0] * (n+2)

  a = []
  inHaku = False
  for _ in range(k):
    x = ni()
    a.append(x)
    kaidan[x] = 1
    if x == 0:
      inHaku = True

  length = []
  tmp = 1
  start = 0
  for i, kai in enumerate(kaidan[1:-1]):
    if kai != 1:
      length.append(tmp - start - 1)
      start = tmp
    tmp += 1
  length += [0]

  # length = []
  # tmp = 0
  # for i, kai in enumerate(kaidan[1:-1]):
  #   if kaidan[i+1] == kai and kai != 0:
  #     tmp += 1
  #   else:
  #     length.append(tmp)
  #     tmp = 0
  # length.append(tmp)
  # length += [0]

  if inHaku:
    ans = 0
    for i in range(len(length)):
      ans = max(ans, sum(length[i:i+2])+1)
    print(ans)
  else:
    print(max(length))

main()