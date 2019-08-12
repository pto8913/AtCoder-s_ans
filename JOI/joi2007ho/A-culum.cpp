#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)

int main(){
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  rep(i, n) cin >> v[i];

  vector<int> wa(n+1);
  rep(i, n){
    wa[i+1] = wa[i] + v[i];
  }

  int ma = 0;
  rep(i, n-k+1){
    ma = max(wa[i+k] - wa[i], ma);
  }
  cout << ma << endl;
}
