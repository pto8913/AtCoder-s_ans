# URL: https://atcoder.jp/contests/abc112/tasks/abc112_c

N = int(input())
xyh = [list(map(int,input().split())) for _ in range(N)]
xyh = sorted(xyh, key = lambda x:-x[2])
mx, my, mh = xyh[0]
for Cx in range(101):
  for Cy in range(101):
    H = mh+abs(mx-Cx)+abs(my-Cy)
    if(all(h == max(0, H-abs(x-Cx)-abs(y-Cy)) for x,y,h in xyh)):
      print(Cx,Cy,H)
      exit()
