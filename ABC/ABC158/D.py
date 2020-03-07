import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def main():
    s = ns()
    Q = ni()

    T1 = 0
    FrontS = ""
    BackS = ""
    for _ in range(Q):
        T = stdin.readline().split()
        if T[0] == "1":
            FrontS, BackS = BackS, FrontS
            T1 += 1
        else:
            if T[1] == "1":
                FrontS += T[2]
            else:
                BackS += T[2]
                
    FrontS = FrontS[::-1]

    if T1 % 2 == 0:
        print(FrontS + s + BackS)
    else:
        print(FrontS + s[::-1] + BackS)

if __name__ == '__main__':
    main()
