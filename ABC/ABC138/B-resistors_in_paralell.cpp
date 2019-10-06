#include <iostream>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)

int main(){
  int n;
  cin >> n;

  int x;
  double ans = 0;
  rep(i, n) {
    cin >> x;
    ans += (double)1 / x;
  }
  printf("%.9f\n", 1 / ans);
}