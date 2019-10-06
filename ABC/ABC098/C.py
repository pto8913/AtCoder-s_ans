# URL: https://atcoder.jp/contests/abc098/tasks/arc098_a

N = int(input())
S = input()

e = S.count("E")
w = 0
ans = e
for s in S:
  if(s == "E"):
    e -= 1
  else:
    w += 1
  ans = min(ans, e+w)
print(ans)
