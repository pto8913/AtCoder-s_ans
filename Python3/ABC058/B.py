# URL: https://atcoder.jp/contests/abc058/tasks/abc058_b

O = input()
E = input()
ans = ""
for i in range(len(O)):
  ans += O[i]
  if(i < len(E)):
    ans += E[i]
print(ans)
