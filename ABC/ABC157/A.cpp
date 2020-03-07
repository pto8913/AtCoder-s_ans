#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int n;
    cin >> n;

    int ans = n / 2;
    if (n % 2 == 0) cout << ans << endl;
    else cout << ans + 1 << endl;
}