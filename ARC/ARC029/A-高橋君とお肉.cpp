#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;
  
  int t[50];
  rep(i, 0, n) cin >> t[i];

  int ans = 1e9;
  rep(i, 0, 1 << n) {
    int a = 0, b = 0;
    rep(j, 0, n) {
      if ((i >> j) & 1) {
        a += t[j];
      } else {
        b += t[j];
      }
    }
    ans = min(ans, max(a, b));
  }
  cout << ans << endl;
}