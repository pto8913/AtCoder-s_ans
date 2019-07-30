# URL: https://atcoder.jp/contests/abc115/tasks/abc115_b

N = int(input())
H = sorted([int(input()) for _ in range(N)])
print(H[-1]//2+sum(H[:-1]))
