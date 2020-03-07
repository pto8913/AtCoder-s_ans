#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;

  vector<int> x(n);
  rep(i, 0, n) cin >> x[i];

  long long Min = (int)1e9+7;
  rep(i, 0, 101)
  {
    long long Sum = 0;
    rep(j, 0, n)
    {
      Sum += pow(x[j] - i, 2);
    }
    if (Min > Sum)
    {
      Min = Sum;
    }
  }
  cout << Min << endl;
}