import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    n = ni()

    for i in range(1, n+1):
        if int(i*1.08) == n:
            print(i)
            return
    print(":(")

if __name__ == '__main__':
  main()
