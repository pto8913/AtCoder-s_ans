# URL: https://atcoder.jp/contests/abc100/tasks/abc100_c

N = int(input())
A = list(map(int,input().split()))

cnt = 0
for a in A:
  while a%2 == 0:
    a //= 2
    cnt += 1
print(cnt)
