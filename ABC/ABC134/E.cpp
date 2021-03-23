#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
typedef long long ll;

int main(){
    ll n;
    cin >> n;

    ll count = 0;
    ll a;
    vector<ll> Vec(n, -1);
    rep(i, 0, n)
    {
        cin >> a;
        rep(j, 0, n)
        {
            if (Vec[j] < a) Vec[j] = a;
        }
    }
    for (ll Elem : Vec)
    {
        if (Elem != -1) ++count;
    }

    cout << count << endl;
}