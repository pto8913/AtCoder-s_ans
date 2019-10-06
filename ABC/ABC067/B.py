# URL: https://atcoder.jp/contests/abc067/tasks/abc067_b

N, M = map(int,input().split())
L = sorted(list(map(int,input().split())))
print(sum(L[-M:]))
