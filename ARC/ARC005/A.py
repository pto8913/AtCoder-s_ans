import sys

stdin = sys.stdin

sn = lambda : stdin.readline().rstrip()
an = lambda : stdin.readline().split()
ni = lambda : int(sn())

takahashi = ("TAKAHASHIKUN", "Takahashikun", "takahashikun")

def main():
  n = ni()

  w = an()

  cnt = 0
  for i, e in enumerate(w):
    if i == n-1:
      e = e[:-1]
    
    if e in takahashi:
      cnt += 1
  
  print(cnt)

main()