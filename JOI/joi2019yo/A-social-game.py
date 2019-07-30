A, B, C = map(int,input().split())

d = 0
cnt = 0
coin = 0
while C > coin:
  d += 1
  cnt += 1
  coin += A
  if d > 6:
    coin += B
    d = 0
print(cnt)