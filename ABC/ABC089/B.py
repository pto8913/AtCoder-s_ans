# URL: https://atcoder.jp/contests/abc089/tasks/abc089_b

N = int(input())
S = input().split()
if(len(set(S)) == 4):
  print("Four")
else:
  print("Three")
