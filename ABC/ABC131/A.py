S = input()

memo = ""
ans = "Good"
for s in S:
  if not memo:
    memo = s
  else:
    if memo == s:
      ans = "Bad"
  memo = s
print(ans)
