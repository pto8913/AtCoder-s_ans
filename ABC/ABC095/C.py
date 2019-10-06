# URL: https://atcoder.jp/contests/abc095/tasks/arc096_a

A, B, C, X, Y = map(int,input().split())
ans = A*X + B*Y
ans = min(ans, C*X*2 + B*max(0, Y-X))
ans = min(ans, C*Y*2 + A*max(0, X-Y))
print(ans)
