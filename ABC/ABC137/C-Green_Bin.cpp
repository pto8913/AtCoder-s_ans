#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)
#define ll long long

int main(){
  int n;
  cin >> n;
  
  string s;
  map<string, int> d;
  rep(i, n) {
    cin >> s;
    sort(s.begin(), s.end());
    ++d[s];
  }
  
  ll ans = 0;
  for (auto p : d) {
    ans += (ll)p.second*(p.second-1)/2;
  }
  cout << ans << endl;
}