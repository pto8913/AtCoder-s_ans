#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
typedef long long ll;

bool comp(ll& a, ll& b)
{
  return a > b;
}

int main(){
  ll x, y, z, k;
  cin >> x >> y >> z >> k;

  vector<ll> A(x), B(y), C(z);
  rep(i, 0, x) scanf("%lld", &A[i]);
  rep(i, 0, y) scanf("%lld", &B[i]);
  rep(i, 0, z) scanf("%lld", &C[i]);
  sort(begin(A), end(A), comp);
  sort(begin(B), end(B), comp);
  sort(begin(C), end(C), comp);

  vector<ll> res;
  rep(l, 0, x)
  {
    rep(m, 0, y)
    {
      rep(n, 0, z)
      {
        if ((l + 1) * (m + 1) * (n + 1) <= k)
        {
          res.push_back(A[l] + B[m] + C[n]);
        }
        else 
        {
          break;
        }
      }
    }
  }
  sort(begin(res), end(res), comp);

  rep(i, 0, k)
  {
    cout << res[i] << endl;
  }
}