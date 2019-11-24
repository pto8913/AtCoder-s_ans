import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
  h, w, k, v = na()

  a = na()

  wa = [0] * (w + 1)
  for i in range(w):
    wa[i + 1] = wa[i] + a[i]
  
  ans = 0
  for i in range(w):
    for j in range(i+1, w+1):
      x =(wa[j] - wa[i]) + (j - i) * k
      if x <= v:
        ans = max(ans, j - i)

  print(ans)


if __name__ == '__main__':
  main()
  