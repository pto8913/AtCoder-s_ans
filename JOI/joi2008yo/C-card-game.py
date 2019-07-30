N = int(input())
A = [int(input()) for _ in range(N)]

taro = A[:]
hana = [i for i in range(1,2*N+1) if i not in A]

place = 0
i = 1
while taro and hana:
  x = min(taro)
  y = min(hana)
  if i%2:
    if not place:
      place = x
      taro.remove(x)
    else:
      a = [t for t in taro if t > place] 
      if a:
        place = min(a)
        taro.remove(min(a))
      else:
        place = 0
  else:
    if not place:
      place = y
      hana.remove(y)
    else:
      a = [h for h in hana if h > place] 
      if a:
        place = min(a)
        hana.remove(min(a))
      else:
        place = 0
  i += 1
print(len(hana))
print(len(taro))
