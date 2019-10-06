#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, y;
  scanf("%d%d", &n, &y);

  rep(i, 0, n+1) {
    rep(j, 0, n+1) {
      int k = n - i - j;
      if (i*10000 + j*5000 + k*1000 == y && k >= 0) {
        printf("%d %d %d\n", i, j, k);
        exit(0);
      }
    }
  }
  printf("-1 -1 -1\n");
}