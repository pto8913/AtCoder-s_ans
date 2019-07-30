N, K = map(int,input().split())
S = input()

res = [0]*N
if S[0] == "(":
  res[0] = 1
else:
  res[0] = -1
for i in range(N-1):
  if S[i+1] == "(":
    res[i+1] = res[i] + 1
  if S[i+1] == ")":
    res[i+1] = res[i] - 1
res.sort(reverse = True)
print(sum(res[:K]))
