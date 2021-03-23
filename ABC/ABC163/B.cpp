#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i=a; i<(n); ++i)
typedef long long ll;

int main()
{
    int n, m ;
    cin >> n >> m;

    ll SumOfWorkDays = 0;
    vector<int> a(m);
    rep(i, 0, m) 
    {
        cin >> a[i];
        SumOfWorkDays += a[i];
    }

    if (n >= SumOfWorkDays)
    {
        printf("%d", n - SumOfWorkDays);
    }
    else
    {
        printf("%d", -1);
    }
}