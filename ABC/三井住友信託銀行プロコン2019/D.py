// python was TLE ;(

#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main()
{
    int n;
    string s;
    cin >> n >> s;

    int cnt = 0;
    rep(i, 0, 1000)
    {
        int tmp[3] = { i/100, (i/10)%10, i%10 };
        int idx = 0;
        rep(j, 0, n)
        {
            if (tmp[idx] == (s[j] + '0')) ++idx;
            if (idx == 3) break;
        }
        if (idx == 3) ++cnt;
    }
    cout << cnt << endl;
}