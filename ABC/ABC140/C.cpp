#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;
  vector<int> b(n, 1e6);
  rep(i, 0, n - 1) cin >> b[i];
  int ans = b[0];
  rep(i, 0, n - 1) {
    ans += min(b[i + 1], b[i]);
  }
  cout << ans << endl;
}