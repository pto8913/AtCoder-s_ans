# uRL: https://atcoder.jp/contests/abc061/tasks/abc061_b

N, M = map(int,input().split())

edges = [0 for _ in range(N)]
for _ in range(M):
  a, b = map(int,input().split())
  edges[a-1] += 1
  edges[b-1] += 1
for edge in edges:
  print(edge)
