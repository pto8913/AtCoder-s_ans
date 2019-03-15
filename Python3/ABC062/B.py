# URL: https://atcoder.jp/contests/abc062/tasks/abc062_b

H, W = map(int,input().split())

result = ["#"*(W+2)]
for _ in range(H):
  c = input()
  result.append("#"+c+"#")
result.append("#"*(W+2))
print("\n".join(result))
