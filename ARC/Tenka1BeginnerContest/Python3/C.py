N = int(input())
S = input()
  
v = [S.count(".")]
for i in range(N):
  if S[i] == "#":
    v.append(v[i]+1)
  else:
    v.append(v[i]-1)
print(min(v))
