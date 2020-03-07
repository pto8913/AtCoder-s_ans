#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int a[9];
    rep(i, 0, 9) cin >> a[i];

    bool reach[9] = {false};
    int n, b;
    cin >> n;
    rep(i, 0, n)
    {
        cin >> b;
        rep(j, 0, 9)
        {
            if (b == a[j]) {
                reach[j] = true;
                break;
            }
        }
    }
    string ans = "No";
    const int yoko[3] = {0, 3, 6};
    rep(i, 0, 3)
    {
        int count = 0;
        rep(j, yoko[i], yoko[i]+3)
        {
            count += reach[j];
        }
        if (count == 3)
        {
            ans = "Yes";
        }
        count = 0;
        for(int j = i; j <= i+6; j+=3)
        {
            count += reach[j];
        }
        if (count == 3)
        {
            ans = "Yes";
        }
    }
    if (reach[0] && reach[4] && reach[8]) ans = "Yes";
    if (reach[2] && reach[4] && reach[6]) ans = "Yes";

    cout << ans << endl;
}