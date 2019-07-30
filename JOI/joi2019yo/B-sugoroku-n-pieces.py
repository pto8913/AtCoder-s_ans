N = int(input())
X = list(map(int,input().split()))
M = int(input())
A = [int(i)-1 for i in input().split()]

for a in A:
  if X[a]+1 not in X and X[a]+1 != 2020:
    X[a] += 1
print("\n".join(list(map(str, X))))