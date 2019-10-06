# URL: https://atcoder.jp/contests/abc082/tasks/arc087_a

from collections import Counter

N = int(input())
A = list(map(int,input().split()))

a = Counter(A)
cnt = 0
for k, v in a.items():
  if(k > v):
    cnt += v
  elif(k < v):
    cnt += v-k
print(cnt)
