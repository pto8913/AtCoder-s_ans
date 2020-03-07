#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, r;
  cin >> n >> r;
  if (n < 10)
  {
    cout << 100 * (10 - n) + r << endl;
  }
  else
  {
    cout << r << endl;
  }
}