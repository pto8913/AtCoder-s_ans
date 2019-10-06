# URL: https://atcoder.jp/contests/abc113/tasks/abc113_b

N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
ans = 1e9
for h in H:
  x = abs(T-h*0.006-A)
  if(ans > x):
    tmp = h
    ans = x
print(H.index(tmp)+1)
