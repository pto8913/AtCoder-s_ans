# URL: https://atcoder.jp/contests/abc123/tasks/abc123_c

N, A, B, C, D, E = [int(input()) for _ in range(6)]
min_ = min(A,B,C,D,E)
print((N+(min_-1))//min_+4)
