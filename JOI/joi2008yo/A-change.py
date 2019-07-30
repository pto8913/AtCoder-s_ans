N = int(input())

money = 1000-N
cnt = 0
for n in [500, 100, 50, 10, 5, 1]:
  cnt += money//n
  money -= n*(money//n)
print(cnt)