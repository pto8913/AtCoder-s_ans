#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)
#define rep1(i) for(int i = -1; i < 2; ++i)

typedef long long ll;
typedef vector<tuple<ll, ll, ll>> vl;

int main(){
  int n, m;
  cin >> n >> m;
  vl v;
  ll x, y, z;
  rep(i, n){
    cin >> x >> y >> z;
    v.emplace_back(x, y, z);
  }
  ll ans = 0;
  rep1(i){
    rep1(j){
      rep1(k){
        vector<ll> s;
        for (auto x : v){
          s.push_back(get<0>(x) * i + get<1>(x) * j + get<2>(x) * k);
        }
        ll tmp = 0;
        sort(s.begin(), s.end(), greater<ll>());
        rep(i, m) tmp += s[i];
        ans = max(ans, tmp);
      }
    }
  }
  cout << ans << endl;
}
