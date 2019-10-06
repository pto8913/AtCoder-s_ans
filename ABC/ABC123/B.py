URL: https://atcoder.jp/contests/abc123/tasks/abc123_b

A, B, C, D, E = [input() for _ in range(5)]
L = [A, B, C, D, E]
ans = 0
tmp = []
for l in L:
  if l[-1] != "0":
    tmp.append(l)
  else:
    ans += int(l)
if tmp:
  tmp.sort(key = lambda x: x[-1] if x[-1] != "0" else "")
  ans += int(tmp[0])
  for t in tmp[1:]:
    ans += (int(t)//10+1)*10
print(ans)
