S = [int(input()) for _ in range(5)]
S = sum([x if x >= 40 else 40 for x in S])
print(S//5)