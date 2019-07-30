L, A, B, C, D = [int(input()) for _ in range(5)]
print(L-max((A+C-1)//C, (B+D-1)//D))