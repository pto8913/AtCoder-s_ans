#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int n, k;
    cin >> n >> k;

    vector<long long> h(n);
    rep(i, 0, n) cin >> h[i];

    sort(h.begin(), h.end());

    vector<long long> wa(n+1);
    rep(i, 0, n) wa[i+1] = wa[i] + h[i];

    long long ans = 1e9+7;
    rep(i, 0, n-k+1)
    {
        long long next = wa[i+k] - wa[i];
        if (ans > next)
        {
            ans = next;
        }
    }
    cout << ans << endl;
}