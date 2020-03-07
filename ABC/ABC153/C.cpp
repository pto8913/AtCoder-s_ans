#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, k;
  cin >> n >> k;
  vector<long long> h(n);
  long long ans = 0;
  if (k >= n) {
    cout << 0 << endl;
    return 0;
  }
  rep(i, 0, n)
  {
    cin >> h[i];
    ans += h[i];
  } 
  sort(h.begin(), h.end());
  for (int i = n-1; i > n-k-1; --i)
  {
    ans -= h[i];
  }
  cout << ans << endl;
}