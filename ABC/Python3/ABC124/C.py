S = input()

if S[0] == "1":
  print(S[::2].count("0")+S[1::2].count("1"))
else:
  print(S[::2].count("1")+S[1::2].count("0"))
