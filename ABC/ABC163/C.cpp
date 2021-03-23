#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define rep(i, a, n) for(int i=a; i<(n); ++i)
typedef long long ll;

int main()
{
    int n;
    cin >> n;

    vector<int> a(n);
    map<int, int> Syain;
    rep(i, 0, n) 
    {
        cin >> a[i];
        ++Syain[a[i] - 1];
    }

    rep(i, 0, n)
    {
        cout << Syain[i] << endl;
    }
}