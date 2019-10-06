import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

def main():
  n = ni()
  s = sn()

  i, j = 0, 1
  ans = 0
  while j < n:
    if s[i:j] in s[j:]:
      ans = max(ans, len(s[i:j]))
      j += 1
    else:
      i += 1
    if i == j:
      i += 1
      j += 2
  print(ans)

main()
