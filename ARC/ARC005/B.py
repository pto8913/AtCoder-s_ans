import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : stdin.readline().split()
ni = lambda : int(sn())

x, y, W = an()
x = int(x) - 1
y = int(y) - 1

ran = []
for _ in range(9):
  s = sn()
  ran.append(s[:0:-1] + s + s[-2::-1])
ran = ran[:0:-1] + ran + ran[-2::-1]
tenti = ["".join(list(r)) for r in zip(*ran)]

if "R" in W:
  if x + 4 > 9:
    print(ran[y][x:] + ran[y][-(x+4)%9:][::-1])
  else:
    print(ran[y][x:x+4])
elif "L" in W:
  if x - 4 < 0:
    print(ran[y][:x][::-1] + ran[y][:abs(x-4)%9])
  else:
    print(ran[y][x-4:x][::-1])
elif "U" in W:
  if y + 4 > 9:
    print(tenti[x][:y][::-1] + tenti[x][:abs(y-4)%9])
  else:
    print(tenti[x][y-4:y][::-1])
if "D" in W and y - 4 < 0:
  isReturn = True

