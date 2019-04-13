def main():
  from itertools import groupby

  N, K = map(int,input().split())
  S = input()

  num = []
  cot = []
  for k, n in groupby(S):
    num.append(k)
    cot.append(len(list(n)))

  if num[-1] == "0":
    cot += [0]
    num += [0]

  X = [0]*(len(cot)+1)
  for i in range(len(cot)):
    X[i+1] = X[i]+cot[i]

  ans = 0
  for i in range(len(X)):
    x = K*2
    if num[i] == "1":
      x += 1
    try:
      ans = max(ans, X[i+x]-X[i])
    except:
      break
  if ans == 0:
    ans = len(S)
  print(ans)

if __name__ == '__main__':
  main()
