N =  int(input())
S = [input() for _ in range(N)]

cnt = 0
b, a = 0, 0
ab = 0
for s in S:
  cnt += s.count("AB")
  if s[0] == "B" and s[-1] == "A":
    ab += 1
  elif s[0] == "B":
    b += 1
  elif s[-1] == "A":
    a += 1
if ab > 1:
  cnt += ab-1
  ab = 1
if ab:
  if a:
    cnt += 1
    a -= 1
  if b:
    cnt += 1
    b -= 1
at = 0
bt = 0
while a > 0 and b > 0:
  if a:
    at += 1
    a -= 1
  if b:
    bt += 1
    b -= 1
  if at + bt == 2:
    cnt += 1
  at = 0
  bt = 0
print(cnt)
