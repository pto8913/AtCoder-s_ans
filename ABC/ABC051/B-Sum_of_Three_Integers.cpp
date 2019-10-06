#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int k, s;
  scanf("%d%d", &k, &s);

  int ans = 0;
  rep(x, 0, k+1) {
    rep(y, 0, k+1) {
      int z = s - x - y;
      if (x + y + z == s && z >= 0 && z <= k) {
        ++ans;
      }
    }
  }
  printf("%d\n", ans);
}