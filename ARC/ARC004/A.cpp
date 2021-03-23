#include <iostream>
#include <vector>
#include <math.h>

using namespace std;


#define rep(i, a, n) for(int i = a; i < (n); ++i)

struct P { int a; int b; };

int main(){
    int n;
    cin >> n;

    vector<P> Vec(n);
    rep(i, 0, n) cin >> Vec[i].a >> Vec[i].b;

    double ans = 0;
    rep(i, 0, n)
    {
        rep(j, i+1, n)
        {
            double x = pow(pow(Vec[j].a - Vec[i].a, 2) + pow(Vec[j].b - Vec[i].b, 2), 0.5);
            ans = max(ans, x);
        }
    }
    cout << ans << endl;
}