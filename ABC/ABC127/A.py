A, B = map(int,input().split())

ans = 0
if A >= 13:
  ans += B
elif 6 <= A <= 12:
  ans += B//2
print(ans)
