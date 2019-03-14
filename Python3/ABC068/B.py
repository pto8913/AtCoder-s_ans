# URL: https://atcoder.jp/contests/abc068/tasks/abc068_b

N = int(input())

tmp = 0
for i in range(2,N+1,2):
  cnt = 0
  while True:
    if(i%2 != 0):
      break
    cnt += 1
    i //= 2
  tmp = max(tmp, cnt)
print(2**tmp)
