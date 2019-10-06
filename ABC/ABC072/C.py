# URL: https://atcoder.jp/contests/abc072/tasks/arc082_a

N = int(input())
A = list(map(int,input().split()))
result = [0]*(10**5+10)
for a in A:
  result[a] += 1
  result[a-1] += 1
  result[a+1] += 1
print(max(result))
