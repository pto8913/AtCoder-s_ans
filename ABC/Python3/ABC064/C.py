# URL: https://atcoder.jp/contests/abc064/tasks/abc064_c

N = int(input())
A = list(map(int,input().split()))

check = set()
free = 0
for a in A:
  x = (a-a%400)//400
  if(x < 8):
    check.add(x)
  else:
    free += 1
c = len(check) 
if(c == 0):
  print(1, free)
else:
  print(c, c+free)
