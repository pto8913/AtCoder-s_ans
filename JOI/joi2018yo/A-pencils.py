N, A, B, C, D = map(int,input().split())
print(min((N+A-1)//A*B, (N+C-1)//C*D))