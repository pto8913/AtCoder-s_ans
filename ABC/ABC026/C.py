import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : list(map(int, stdin.readline().split()))
ni = lambda : int(sn())

def main():
  n = ni()
  b = [[[], 0] for _ in range(n + 1)]
  for i in range(1, n):
    value = ni()
    b[value][0] += [i + 1]

  for i in range(n, 0, -1):
    if b[i][0] == []:
      b[i][1] = 1
    elif len(b[i][0]) == 1:
      b[i][1] = b[b[i][0][0]][1] * 2 + 1    
    else:
      max_tmp = 0
      min_tmp = 1e9
      for bb in b[i][0]:
        max_tmp = max(b[bb][1], max_tmp)
        min_tmp = min(b[bb][1], min_tmp)
      #print(max_tmp, min_tmp)
      b[i][1] = max_tmp + min_tmp + 1
  #print(b)
  print(b[1][1])

main()
