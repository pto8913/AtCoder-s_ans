# URL: https://atcoder.jp/contests/abc120/tasks/abc120_c

S = input()
zero = S.count("0")
one = S.count("1")
print(min(zero, one)*2)
