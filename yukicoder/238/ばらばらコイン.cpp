#include <iostream>

using namespace std;

int main(){
  int n, k;
  cin >> n >> k;

  if (n < k) {
    cout << -1 << endl;
    return 0;
  }
  cout << k - 1 << endl;
  return 0;
}