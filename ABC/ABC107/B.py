# URL: https://atcoder.jp/contests/abc107/submissions/me

H, W = map(int,input().split())
HW = [input() for _ in range(H)]
HW = ["".join(hw) for hw in zip(*HW) if hw.count("#") > 0]
HW = ["".join(hw) for hw in zip(*HW) if hw.count("#") > 0]
print("\n".join(HW))
