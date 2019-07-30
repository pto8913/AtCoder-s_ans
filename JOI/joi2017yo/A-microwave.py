A, B, C, D, E = [int(input()) for _ in range(5)]
time = 0
if A < 0:
  time = abs(A)*C+D
  A = 0
if A == 0:
  time += B*E
else:
  time += (B-A)*E
print(time)