# URL: https://atcoder.jp/contests/abc077/tasks/arc084_a

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
a, c, cnt = 0, 0, 0
for b in B:
  while a < N and A[a] < b:
    a += 1
  while c < N and C[c] <= b:
    c += 1
  cnt += a * (N-c)
print(cnt)
