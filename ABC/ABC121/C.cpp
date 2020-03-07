#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define ll long long

template<class T, class U>
struct P { T a; U b; };

bool Comp(P<ll, ll>& a, P<ll, ll>& b)
{
  return a.a < b.a;
}

int main(){
  ll n, m;
  cin >> n >> m;

  vector<P<ll, ll>> ab(n);
  rep(i, 0, n) cin >> ab[i].a >> ab[i].b;
  sort(ab.begin(), ab.end(), Comp);
  
  ll a, b, ans = 0;
  rep(i, 0, n)
  {
    a = ab[i].a; 
    b = ab[i].b;
    if (m <= b)
    {
      ans += m * a;
      break;
    }
    if (m > b)
    {
      m -= b;
      ans += a * b;
    }
  }
  printf("%lld\n", ans);
}