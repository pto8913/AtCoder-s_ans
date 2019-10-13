import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  n, m = na()

  graph = [set() for _ in range(n + 1)]
  for _ in range(m):
    a, b = na()
    graph[b].add(a)
  
  for i in range(1, n + 1):
    if not graph[i]:
      print(i)
      return
      
main()