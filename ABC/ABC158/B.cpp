#include <iostream>
#include <math.h>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
    long long n, a, b;
    cin >> n >> a >> b;
	
    if (a == 0 && b == 0 || a == 0) 
    {
      cout << 0 << endl;
      return 0;
    }
    if (n < a + b)
    {
        cout << min(n, a) << endl;
        return 0;
    }

    long long x = n / (a + b);
    cout << x * a + n - (a + b) << endl;
}
