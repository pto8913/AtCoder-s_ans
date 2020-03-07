import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : stdin.readline().split()
sys.setrecursionlimit(10 ** 7)

def main():
    n = ni()
    s, t = na()

    tmp = ""
    for i, ss in enumerate(s):
        tmp += ss + t[i]
    print(tmp)



if __name__ == '__main__':
    main()
