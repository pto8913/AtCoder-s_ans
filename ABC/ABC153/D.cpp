#include <iostream>
#include <math.h>

using namespace std;

// 2^1 = 3 2^2 = 7 2^3 = 15
// 2^(n+1)-1
// 10^12 < 2^40
#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  long long h;
  cin >> h;

  long long pre = 1, next = 1;
  long long ans = 1;
  rep(i, 1, 41)
  {
    next = pow(2, i);
    if (next == h) {
      ans = pow(2, i+1) - 1;
      break;
    }
    if (pre < h && h < next)
    {
      ans = pow(2, i) - 1;  
      break;
    }
    pre = next;
  }
  cout << ans << endl;
}