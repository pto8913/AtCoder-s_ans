def ans():
  import sys
  input = sys.stdin.readline

  N, _ = map(int,input().split())
  P = [int(i)-1 for i in input().split()]
  ABC = [[int(i) for i in input().split()]for _ in range(N-1)]

  usedRail = [0]*N
  for pre, nex in zip(P, P[1:]):
    if pre > nex:
      pre, nex = nex, pre
    usedRail[pre] += 1
    usedRail[nex] -= 1

  res = [0]
  for use in usedRail:
    res.append(res[-1]+use)

  cost = 0
  for i, (a, b, c) in enumerate(ABC):
    cost += min(a*res[i+1], c+b*res[i+1])
  print(cost)

if __name__ == "__main__":
  ans()