# URL: https://atcoder.jp/contests/abc109/tasks/abc109_b

N = int(input())
memo = []
ans = "Yes"
for _ in range(N):
  W = input()
  if(memo == []):
    memo.append(W)
  elif(W in memo or memo[-1][-1] != W[0]):
    ans = "No"
  else:
    memo.append(W)
print(ans)
