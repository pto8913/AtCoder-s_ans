S = input()
if len(set(S)) == 2:
  if S.count(S[0]) == 2 and S.count(S[1]) == 2:
    print("Yes")
    exit()
print("No")
