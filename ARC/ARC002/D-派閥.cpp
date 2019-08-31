#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define size_of_array(array) (sizeof(array) / sizeof(array[0]))

int main(){
  int n, m;
  cin >> n >> m;

  vector<ll> habatu[11111];
  rep(i, 0, m) {
    ll x, y;
    cin >> x >> y;
    habatu[x].push_back(y);
    habatu[y].push_back(x);
  }
  ll ans = 0;
  rep(i, 0, m) {
    ans = max(ans, size_of_array(habatu[i+1]) + 1);
  }
  cout << ans << endl;
}