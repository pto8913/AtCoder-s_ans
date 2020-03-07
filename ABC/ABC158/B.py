import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    n, a, b = na()
    
    if (a == 0 and b == 0) or a == 0:
        print(0)
        return

    if n <= a:
        print(n)
        return
      
    AB = a + b
    if n <= AB:
        print(min(n, a))
        return 
    
    x = int(n / AB)

    print(x * a + min(n - (x * AB), a))

if __name__ == '__main__':
    main()
