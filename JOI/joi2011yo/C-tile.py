N = int(input())
M = int(input())
AB = [[int(i)-1 for i in input().split()]for _ in range(M)]

for a, b in AB:
  mid = (N-1)//2
  if a > mid:
    a = N-a-1
  if b > mid:
    b = N-b-1
  
  tmp = max(mid-a, mid-b)
  check = (N+1)//2%3
  if check == 0:
    print(3-tmp%3)
  elif check == 1:
    print(3-(tmp+2)%3)
  else:
    print(3-(tmp+1)%3)