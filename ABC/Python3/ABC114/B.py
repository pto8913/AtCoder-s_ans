# URL: https://atcoder.jp/contests/abc114/tasks/abc114_b

S = input()
ans = 1e9
for i in range(len(S)-2):
  ans = min(ans, abs(753-int(S[i:i+3])))
print(ans)
