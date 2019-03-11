# URL: https://atcoder.jp/contests/abc081/tasks/abc081_b

N = int(input())
A = list(map(int,input().split()))

cnt = 0
while all(a%2 == 0 for a in A):
  A = list(map(lambda x: x//2, A))
  cnt += 1
print(cnt)
