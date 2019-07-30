num = [int(input()) for _ in range(28)]
for n in range(1, 31):
  if n not in num:
    print(n)