# URL: https://atcoder.jp/contests/abc104/tasks/abc104_b

S = input()
ans = "WA"
if(S[0] == "A"):
  if(S[2:-1].count("C") == 1):
    if(S[1:S.index("C")].islower() and S[S.index("C")+1:].islower()):
      ans = "AC"
print(ans)

"""
--islower()--

x = "abc"
print(x.islower())
# True

x = "cA"
print(x.islower())
# False

--isupper()--

x = "ABC"
print(x.isupper())
# True

x = "abC"
print(x.isupper())
# False
"""
