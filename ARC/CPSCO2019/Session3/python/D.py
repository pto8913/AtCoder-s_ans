N = int(input())
S = input()

ans = "No"
if S[0] == "R" and S[-1] == "B" and "GG" not in S and "RB" not in S:
  ans = "Yes"
print(ans)
