# URL: https://atcoder.jp/contests/abc123/tasks/abc123_d

# So slow
def main():
  import sys
  input = sys.stdin.readline
  
  X, Y, Z, K = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))
  C = list(map(int,input().split()))
  A.sort(reverse = True)
  B.sort(reverse = True)
  C.sort(reverse = True)
  AB = [a+b for a in A for b in B]
  AB.sort(reverse = True)
  res = [c+ab for ab in AB[:min(K, len(AB))] for c in C]
  res.sort(reverse = True)
  for r in res[:K]:
    print(r)

if __name__ == "__main__":
  main()

# The following code is base on the explanation
# fast

def main():
  import sys
  input = sys.stdin.readline
  
  X, Y, Z, K = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))
  C = list(map(int,input().split()))
  A.sort(reverse = True)
  B.sort(reverse = True)
  C.sort(reverse = True)
  res = []
  for i in range(X):
    for j in range(Y):
      for k in range(Z):
        if (i+1)*(j+1)*(k+1) <= K:
          res.append(A[i]+B[j]+C[k])
        else:
          break
  res.sort(reverse = True)
  for r in res[:K]:
    print(r)

if __name__ == "__main__":
  main()

# So fast

def main():
  import sys
  from heapq import heappush as hpush, heappop as hpop
  input = sys.stdin.readline
  
  X, Y, Z, K = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))
  C = list(map(int,input().split()))
  A.sort(reverse = True)
  B.sort(reverse = True)
  C.sort(reverse = True)
  
  memo = set([(0, 0, 0)])
  h = [(-(A[0]+B[0]+C[0]), (0, 0, 0))]
  for _ in range(K):
    val, (i,j,k) = hpop(h)
    if i+1 < len(A) and (i+1, j, k) not in memo:
      hpush(h, (-(A[i+1]+B[j]+C[k]), (i+1, j, k)))
      memo.add((i+1, j, k))
    if j+1 < len(B) and (i, j+1, k) not in memo:
      hpush(h, (-(A[i]+B[j+1]+C[k]), (i, j+1, k)))
      memo.add((i, j+1, k))
    if k+1 < len(C) and (i, j, k+1) not in memo:
      hpush(h, (-(A[i]+B[j]+C[k+1]), (i, j, k+1)))
      memo.add((i, j, k+1))
    print(-val)

if __name__ == "__main__":
  main()
