import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    n = ni()

    if n % 2 != 0:
        print(0)
        return
    
    n //= 10
    ans = n
    while n > 0:
        n //= 5
        ans += n
    print(ans)    

if __name__ == '__main__':
    main()

