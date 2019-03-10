# URL: https://atcoder.jp/contests/abc096/tasks/abc096_b

a, b, c = sorted(map(int,input().split()))
K = int(input())

print(2**K*c+a+b)
