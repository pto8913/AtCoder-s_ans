N = int(input())
ST = [list(map(int,input().split())) for _ in range(N)]
ST.sort(key = lambda x: x[0])

cnt = 1
ss, st = ST[0]
for s, t in ST[1:]:
  if ss <= s <= st:
    if t > st:
      st = t
  elif ss <= t <= st:
    continue
  else:
    ss = s
    st = t
    cnt += 1
print(cnt)
