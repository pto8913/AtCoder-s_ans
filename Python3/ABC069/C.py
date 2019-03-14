# URL: https://atcoder.jp/contests/abc069/tasks/arc080_a

N = int(input())
A = list(map(int,input().split()))

tmp = [a%4 for a in A]
four = tmp.count(0)
two = tmp.count(2)

if(four+two//2 >= N//2):
  print("Yes")
else:
  print("No")
