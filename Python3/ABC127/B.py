r, D, x0 = map(int,input().split())

x1 = r*x0-D
l = [x1]
for i in range(10):
  print(l[i])
  l.append(l[i]*r-D)
