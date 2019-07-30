#include <iostream>
#include <string>

using namespace std;

typedef long long Int;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int N;
  cin >> N;
  double ans = 0;
  rep(i, N) {
    double x;
    string y;
    cin >> x >> y;
    if (y == "JPY") ans += x;
    else ans += x*380000.0;
  }
  printf("%.9f", ans);
}
