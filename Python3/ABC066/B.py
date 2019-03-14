# URL: https://atcoder.jp/contests/abc066/tasks/abc066_b

S = input()

tmp = 0
for i in range(len(S)):
  S = S[:-1]
  if(S[:len(S)//2] == S[len(S)//2:]):
    tmp = max(tmp, len(S))
print(tmp)
