# URL: https://atcoder.jp/contests/abc099/tasks/abc099_b

A, B = map(int,input().split())

cnt = 0
for i in range(1,B-A):
  cnt += i
print(cnt-A)
