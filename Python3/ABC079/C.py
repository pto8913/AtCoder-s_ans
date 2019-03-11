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
