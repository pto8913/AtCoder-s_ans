# URL: https://atcoder.jp/contests/abc074/tasks/abc074_b

N = int(input())
K = int(input())
X = list(map(int,input().split()))

dis = 0
for x in X:
  dis += min(abs(K-x), x)*2
print(dis)
