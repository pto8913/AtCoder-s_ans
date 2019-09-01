#include <iostream>
#include <cstring>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define ll long long

int main(){
  char s[10];
  scanf("%s", s);

  int n = strlen(s);
  ll ans = 0;
  rep(bit, 0, 1 << (n-1)) {
    ll tmp = s[0] - '0';
    rep(j, 0, n-1) {
      if ((bit >> j) & 1) {
        ans += tmp;
        tmp = 0;
      }
      tmp = tmp * 10 + s[j+1] - '0';
    }
    ans += tmp;
  }
  printf("%lld\n", ans);
}