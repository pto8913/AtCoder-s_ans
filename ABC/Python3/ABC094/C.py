# URL: https://atcoder.jp/contests/abc094/tasks/arc095_a

N = int(input())
X = list(map(int,input().split()))
sort_X = sorted(X)
a = sort_X[N//2]
b = sort_X[N//2-1]
for x in X:
  if(x <= b):
    print(a)
  else:
    print(b)
