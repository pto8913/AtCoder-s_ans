#include <iostream>

using namespace std;

int main(){
  char S[16];
  cin >> S;
  int cnt = 0;
  for (int i = 0; i < 16; ++i) {
    if (S[i] == 'x') cnt++;
  }
  if (cnt >= 8) cout << "NO" << endl;
  else cout << "YES" << endl;
}
