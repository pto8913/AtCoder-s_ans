# URL: https://atcoder.jp/contests/abc098/tasks/abc098_b

N = int(input())
S = input()
ans = 0
for i in range(N):
  cnt = 0
  l = set(S[:i])
  r = set(S[i:])
  for ll in l:
    if(ll in r):
      cnt += 1
  ans = max(ans, cnt)
print(ans)
