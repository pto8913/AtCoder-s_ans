#include <iostream>
#include <math.h>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  scanf("%d", &n);

  double ans = 0;
  int x[100], y[100];
  rep(i, 0, n) scanf("%d%d", &x[i], &y[i]);

  rep(i, 0, n-1) {
    rep(j, i+1, n) {
      ans = max(ans, pow(pow(x[j]-x[i], 2) + pow(y[j]-y[i], 2), 0.5));
    }
  }
  printf("%.9f\n", ans);
}