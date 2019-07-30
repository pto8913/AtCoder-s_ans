# URL: https://atcoder.jp/contests/abc108/tasks/abc108_b

a, b, c, d = map(int,input().split())
x = c-a
y = d-b
print(c-y, d+x, a-y, b+x)
