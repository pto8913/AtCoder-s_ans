# URL: https://atcoder.jp/contests/abc114/tasks/abc114_c

from itertools import product

N = int(input())
cnt = 0
for i in range(3,len(str(N))+1):
  for p in product(["3", "5", "7"], repeat = i):
    if("3" in p and "5" in p and "7" in p):
      if(int("".join(p)) <= N):
        cnt += 1
print(cnt)
