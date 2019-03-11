# URL: https://atcoder.jp/contests/abc087/tasks/arc090_a

N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
candies = 0
for i in range(N):
  candies = max(candies, sum(A[0][:i+1]) + sum(A[1][i:]))
print(candies)
