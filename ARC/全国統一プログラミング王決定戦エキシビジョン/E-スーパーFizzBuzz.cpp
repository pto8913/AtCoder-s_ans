#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int n;
    cin >> n;

    const int takos[5] = {2, 3, 4, 5, 6};

    const string aiueo = "abcde";
    rep(i, 1, n+1)
    {
        string res = "";
        rep(j, 0, 5)
        {
            if (i % takos[j] == 0)
            {
                res += aiueo[j];
            }
        }
        if (res == "")
        {
            cout << i << endl;
        }
        else
        {
            cout << res << endl;
        }
    }
}