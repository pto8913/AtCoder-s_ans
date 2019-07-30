from collections import Counter

S = input()

tmp = 0
ans = "Yes"
for k, v in Counter(S).most_common():
  if not tmp:
    tmp = v
  elif tmp != v:
    ans = "No"
print(ans)
