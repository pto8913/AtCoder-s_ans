import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def new(t):
    for r in t:
        tmp = []
        cnt = 0
        for b in [100, 101, 102, 103, 104, 105]:
            nex = r - b
            if nex == 0 or r % b == 0:
                return 1
            elif nex < 100:
                cnt += 1
                if cnt == 6:
                    return 0
            tmp.append(nex)
        t = tmp
    # print(t, tmp)
    return new(t)
        

def main():
    x = ni()

    t = [x]
    return new(t)
    

if __name__ == '__main__':
    print(main())