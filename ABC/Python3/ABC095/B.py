# URL: https://atcoder.jp/contests/abc095/tasks/abc095_b

N, X = map(int,input().split())
m = [int(input()) for _ in range(N)]
x = X-sum(m)
print(N+x//min(m))
