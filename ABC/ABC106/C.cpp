#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    string s;
    cin >> s;
    long long k;
    cin >> k;

    rep(i, 0, k)
    {
        if (s[i] != '1')
        {
            cout << s[i];
            return;
        }
        
    }
}