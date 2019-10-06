def main():
  n, k = map(int,input().split())
  s = input()

  from itertools import groupby

  tmp = []
  num = []
  for ke, v in groupby(s):
    num.append(ke)
    tmp.append(len(list(v)))
  
  num += [0]
  tmp += [0]

  nt = len(tmp)
  wa = [0] * (nt+1)
  for i in range(nt):
    wa[i+1] = wa[i] + tmp[i]

  ans = 0
  for i in range(len(wa)):
    x = k*2
    if num[i] == "1":
      x += 1
    try:
      ans = max(ans, wa[i+x] - wa[i])
    except:
      break
  if not ans:
    ans = len(s)
  print(ans)

main()
