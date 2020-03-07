#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    string S;
    cin >> S;

    bool IsA = false;
    bool IsB = false;
    rep(i, 0, S.length())
    {
        if (S[i] == 'A') IsA = true;
        if (S[i] == 'B') IsB = true;
    }
    if (IsA && IsB) cout << "Yes" << endl;
    else cout << "No" << endl;
}