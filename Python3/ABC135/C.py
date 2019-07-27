def main():
  N = int(input())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))

  cnt = 0
  for i in range(N):
    if B[i] - A[i] >= 0:
      cnt += A[i]
      B[i] -= A[i]
      A[i] = 0
    elif B[i] - A[i] < 0:
      cnt += B[i]
      tmp = B[i]
      B[i] = 0
      A[i] -= tmp
    if B[i] == 0:
      continue
    if B[i] - A[i+1] >= 0:
      cnt += A[i+1]
      B[i] -= A[i+1]
      A[i+1] = 0
    elif B[i] < A[i+1]:
      cnt += B[i]
      tmp = B[i]
      B[i] = 0
      A[i+1] -= tmp
  print(cnt)

if __name__ == "__main__":
  main()
