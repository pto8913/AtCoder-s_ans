# URL: https://atcoder.jp/contests/abc076/tasks/abc076_c

S = input()
T = input()
ans = "UNRESTORABLE"
for i in range(len(S)-len(T)+1):
  for j in range(len(T)):
    if(T[j] == S[i+j] or S[i+j] == "?"):
      continue
    else:
      break
  else:
    ans = S[:i]+T+S[i+len(T):]
    ans = ans.replace("?", "a")
print(ans)
