import sys 
stdin = sys.stdin
sn = lambda : stdin.readline().rstrip()
ni = lambda : int(sn())
na = lambda : map(int, stdin.readline().split())

n, k = na()
ab = [list(na()) for _ in range(n)]
ab.sort(key = lambda x: -(x[0]-x[1]))
ans = 0
cnt = 0
for a, b in ab:
    if cnt != k:
        cnt += 1
        ans += b
    else:
        ans += a
print(ans)
