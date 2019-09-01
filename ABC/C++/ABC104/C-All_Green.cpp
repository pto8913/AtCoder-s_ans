#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define per(i, a, b) for(int i = a; i > (b); --i)
#define ll long long
#define INF 1000000007

int main(){
  ll d, g;
  scanf("%lld%lld", &d, &g);

  ll p[100], c[100];
  rep(i, 0, d) scanf("%lld%lld", &p[i], &c[i]);

  ll ans = INF;
  rep(bit, 0, 1 << d) {
    ll point = 0, cnt = 0;
    rep(j, 0, d) {
      if ((bit >> j) & 1) {
        point += p[j] * 100 * (j+1) + c[j];
        cnt += p[j];
      }
    }
    per(j, d-1, -1) {
      if ((bit >> j) & 1) continue;
      ll tmp = 0;
      while (tmp + 1 < p[j] && point < g) {
        point += (j + 1) * 100;
        ++cnt;
        ++tmp;
      }
    }
    if (point >= g) {
      ans = min(ans, cnt);
    }
  }
  printf("%lld\n", ans);
}