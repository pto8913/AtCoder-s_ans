#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;
  vector<int> a(n), b(n), c(n - 1);
  rep(i, 0, n) cin >> a[i];
  rep(i, 0, n) cin >> b[i];
  rep(i, 0, n - 1) cin >> c[i];
  
  int ans = 0;
  rep(i, 0, n) {
    if (a[i] + 1 == a[i + 1]) ans += c[a[i] - 1];
    ans += b[a[i] - 1];
  }
  cout << ans << endl;
}