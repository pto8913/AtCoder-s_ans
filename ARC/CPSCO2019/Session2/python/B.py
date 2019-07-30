N = int(input())
CA = [input().split() for _ in range(N)]

M = sum([int(a) for c, a in CA if c == "+"])
mul = 1
for c, a in CA:
  if c == "*":
    if a != "0":
      mul *= int(a)
print(M*mul)
