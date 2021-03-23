import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))
sys.setrecursionlimit(10 ** 7)

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
    n = ni()
    A = []
    Onaji = {}
    for i in na():
        i -= 1
        A.append(i)
        if i in Onaji:
            Onaji[i] += 1
        else:
            Onaji[i] = 1

    kumi = {}
    minuskumi = {}
    Sum = 0
    for a in A:
        if Onaji[a] <= 1:
            continue
        if a in kumi:
            continue
        kumi[a] = cmb(Onaji[a], 2)
        if Onaji[a] - 1 <= 1:
            minuskumi[a] = 0
        else:
            minuskumi[a] = cmb(Onaji[a] - 1, 2)
        Sum += kumi[a]
    # print(Sum)
    # print(kumi)
    # print(minuskumi)
    for a in A:
        if a in minuskumi and a in kumi:
            print(minuskumi[a] + Sum - kumi[a])
        else:
            print(Sum)
    
if __name__ == '__main__':
    main()