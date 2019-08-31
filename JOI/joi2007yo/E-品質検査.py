import sys

stdin = sys.stdin
nl = lambda: map(int, stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(ns())

def main():
  a, b, c = nl()
  n = ni()

  kekka = []
  for _ in range(n):
    kekka.append(list(nl()))
  kekka.sort(key = lambda x : -x[3])

  res = [2] * (a+b+c+1)
  for i, j, k, r in kekka:
    if r == 1:
      res[i] = 1
      res[j] = 1
      res[k] = 1
    elif r == 0:
      if res[i] == 1 and res[j] == 1:
        res[k] = 0
      elif res[i] == 1 and res[k] == 1:
        res[j] = 0
      elif res[j] == 1 and res[k] == 1:
        res[i] = 0
    
  for i in res[1:]:
    print(i)
  
main()