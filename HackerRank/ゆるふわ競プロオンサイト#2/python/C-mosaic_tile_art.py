def main():
  n = int(input())

  mod = int(1e9+7)

  def factorial(n):
    ret = 1
    for i in range(1,n+1):
      ret *= i
      ret %= mod
    return ret

  print(n * factorial(n-1) % mod)

main()
