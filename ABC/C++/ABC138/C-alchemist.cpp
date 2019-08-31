#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)

int main(){
  int n; 
  scanf("%d", &n);

  vector<int> v(n);
  rep(i, n) scanf("%d", &v[i]);

  sort(v.begin(), v.end());

  double ans = (v[0] + v[1]) / 2.0;
  for(int i = 2; i < n; ++i) {
    ans = (ans + v[i]) / 2.0;
  }
  printf("%.5f\n", ans);
}