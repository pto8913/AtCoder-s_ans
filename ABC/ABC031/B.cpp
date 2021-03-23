#include <iostream>

using namespace std;


#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int l, h;
    cin >> l >> h;

    int n;
    cin >> n;

    int a;
    rep(i, 0, n)
    {  
        cin >> a;
        if (a < l)
        {
            cout << l - a << endl;
        }
        else if (l <= a && a <= h)
        {
            cout << 0 << endl;
        }
        else
        {
            cout << -1 << endl;
        }
    }
}