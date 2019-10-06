#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;

  double ans = 0;
  if (n % 2 == 0) {
    cout << ((n / 2) / (double)n) << endl;
  } 
  else {
    cout << (((n / 2) + 1) / (double)n) << endl;
  }
}