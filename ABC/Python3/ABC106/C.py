# URL: https://atcoder.jp/contests/abc106/tasks/abc106_c

S = input()
K = int(input())

for s in S:
  if(s == "1"):
    K -= 1
    if(K == 0):
      print(1)
      break
  else:
    print(s)
    break
