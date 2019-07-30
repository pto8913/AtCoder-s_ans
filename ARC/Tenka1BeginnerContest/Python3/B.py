N = int(input())
S = input()
K = int(input())

t = S[K-1]
ans = ""
for s in S:
  if s != t:
    ans += "*"
  else:
    ans += s
print(ans)
