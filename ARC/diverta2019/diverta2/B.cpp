#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

int main(){
  int N;
  cin >> N;
  vector<ll> x(N), y(N);
  rep(i,N) cin >> x[i] >> y[i];
  map<P, int> mp;
  rep(i,N) {
    rep(j,N) {
      if (i == j) continue;
      ++mp[P(x[i]-x[j], y[i]-y[j])];
  	}
  }
  int res = 0;
  for (auto x: mp){
    res = max(res, x.second);
  }
  cout << N - res << endl;
}
