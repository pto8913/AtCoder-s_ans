#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

template<class T>
int Divisor(T Num)
{
    int res = 0;
    for(T i = 1; i * i <= Num; ++i)
    {
        if (Num % i == 0)
        {
            ++res;
            if (i * i != Num) ++res;
        }
    }
    
    return res;
}

int main(){
    int n;
    cin >> n;
    int ans = 0;
    rep(i, 1, n+1)
    {
        if (i % 2 == 1)
        {
            if (Divisor(i) == 8) ++ans;
        }
    }
    cout << ans << endl;
}
