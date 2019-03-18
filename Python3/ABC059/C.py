# URL: https://atcoder.jp/contests/abc059/tasks/arc072_a

N = int(input())
A = list(map(int,input().split()))

def f(x):
  cnt = 0
  tmp = 0
  for a in A:
    tmp += a
    #print(tmp, x)
    if(tmp*x >= 0):
      cnt += abs(tmp)+1
      tmp = -x
    x *= -1
    #print(tmp, x)
  return cnt

print(min(f(1), f(-1)))  
