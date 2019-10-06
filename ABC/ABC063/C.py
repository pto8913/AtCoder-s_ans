# URL: https://atcoder.jp/contests/abc063/tasks/arc075_a

N = int(input())
S = sorted([int(input()) for _ in range(N)])
sum_ = sum(S)
if(sum_%10 == 0):
  for s in S:
    if(s%10 != 0):
      sum_ -= s
      break
  else:
    sum_ = 0
print(sum_)
