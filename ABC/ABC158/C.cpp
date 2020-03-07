#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    int a, b;
    cin >> a >> b;

    int x = a / 0.08;
    int y = b / 0.1;

    rep(i, min(x, y), max(x, y)*max(x, y))
    {
        if (int(i * 0.08) == a && int(i * 0.1) == b)
        {
            cout << i << endl;
          	return 0;
        }
    }
    cout << -1 << endl;
}