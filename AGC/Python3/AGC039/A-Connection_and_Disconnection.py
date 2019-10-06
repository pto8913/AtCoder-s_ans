import sys

stdin = sys.stdin

ns = lambda : stdin.readline().rstrip()
ni = lambda : int(ns())
na = lambda : list(map(int, stdin.readline().split()))

def main():
  s = ns() + "0"
  k = ni()
  n = len(s) - 1

  if n * s[0] == s[:-1]:
    print((n * k) // 2)
    return

  isSame = True if s[0] == s[-2] else False

  cnt = 1
  w = []
  w_cnt = []
  pre = s[0]
  ans = 0
  tmp = 0
  for i in range(1, n + 1):
    if pre == s[i]:
      cnt += 1
    else:
      w_cnt.append(cnt)
      tmp += cnt // 2
      cnt = 1
      w.append(pre)
      pre = s[i]

  if isSame:
    joins = (w_cnt[0] + w_cnt[-1]) // 2
    ans = 0
    for c in w_cnt[1:-1]:
      ans += c // 2
    print(ans * k + joins * (k - 1) + w_cnt[0] // 2 + w_cnt[-1] // 2)
  else:
    ans = tmp
    print(ans * k)
  # print(w_cnt[1:-1])
  
  # print(isSame)

main()