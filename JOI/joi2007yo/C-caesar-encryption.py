S = input()
A = ord("A")
ans = ""
for s in S:
  ans += chr((ord(s)-A-3)%26+A)
print(ans)