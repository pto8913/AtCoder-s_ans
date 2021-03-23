#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
typedef long long ll;

int main(){
    ll a, b, m;
    cin >> a >> b >> m;
    vector<ll> A(a), B(b);
    ll mina = 1e9+7, minb = 1e9+7;
    rep(i, 0, a) 
    {
        cin >> A[i];
        if (mina > A[i])
        {
            mina = A[i];
        }
    }
    rep(i, 0, b) 
    {
        cin >> B[i];
        if (minb > B[i])
        {
            minb = B[i];
        }
    }
    ll x, y, c;
    ll ans = 1e9+7;
    rep(i, 0, m)
    {
        cin >> x >> y >> c;
        --x; --y;
        ll money = A[x] + B[y] - c;
        if (ans > money)
        {
            ans = money;
        }
    }
    if (ans > mina + minb)
    {
        ans = mina + minb;
    }
    cout << ans << endl;
}