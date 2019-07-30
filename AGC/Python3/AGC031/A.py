# URL: https://atcoder.jp/contests/agc031/tasks/agc031_a

N = int(input())
S = input()

mod = 10**9+7
cnt = 1
setS = set(S)
for s in setS:
  cnt *= S.count(s)+1
print((cnt-1)%mod)
