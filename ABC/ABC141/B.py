import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : map(int, stdin.readline().split())
ni = lambda : int(sn())

s = sn()

odd = s[::2]
even = s[1::2]
ans = "Yes"
for o in odd:
  if o not in ("R", "U", "D"):
    ans = "No"
for e in even:
  if e not in ("L", "U", "D"):
    ans = "No"
print(ans)
