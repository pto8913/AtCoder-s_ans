# URL: https://atcoder.jp/contests/abc066/tasks/abc066_a

a, b, c = map(int,input().split())
print(min(a+b, b+c, c+a))
