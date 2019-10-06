#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define ll long long

int main(){
  int n, k, q;
  cin >> n >> k >> q;

  vector<ll> v(n, k), cnt(n);
  ll a;
  rep(i, 0, q) {
    cin >> a;
    ++cnt[a - 1];
  }
  rep(i, 0, n) {
    if (k + cnt[i] - q  > 0) cout << "Yes" << endl;
    else cout << "No" << endl;
  }
}