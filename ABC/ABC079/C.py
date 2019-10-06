# URL: https://atcoder.jp/contests/abc079/tasks/abc079_c

S = input()
a, b, c, d = S

ops = ["+","-"]
for op1 in ops:
  for op2 in ops:
    for op3 in ops:
      x = a+op1+b+op2+c+op3+d
      if(eval(x) == 7):
        print(x+"=7")
        exit()

        
# bit
S = input()

for i in range(1 << 3):
  tmp = int(S[0])
  op = []
  for j in range(3):
    if ((i >> j) & 1) == 1:
      op += ["+"]
      tmp += int(S[j+1])
    else:
      op += ["-"]
      tmp -= int(S[j+1])
  if tmp == 7:
    res = ""
    for j in range(3):
      res += S[j]+op[j]
    print(res+S[3]+"=7")
    break
