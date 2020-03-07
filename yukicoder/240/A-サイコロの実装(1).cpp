#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    long long n;
    cin >> n;

    if (n % 6 == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
}