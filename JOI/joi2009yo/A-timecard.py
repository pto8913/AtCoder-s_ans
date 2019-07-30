# 1m = 60s : 1h = 60m = 3600s

for _ in range(3):
  a, b, c, d, e, f = map(int,input().split())
  time = (d-a)*3600 + (e-b)*60 + f-c
  print(time//3600, time//60%60, time%60)