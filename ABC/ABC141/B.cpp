#include <iostream>
#include <string>
#include <cstring>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  string s;
  cin >> s;
  
  int n = s.size();
  rep(i, 0, n) {
    if (i % 2 == 0) {
      if (s[i] != 'R' && s[i] != 'U' && s[i] != 'D') {
        cout << "No" << endl;
        return 0;
      }
    }
    else {
      if (s[i] != 'L' && s[i] != 'U' && s[i] != 'D') {
        cout << "No" << endl;
        return 0;
      }
    }
  }
  cout << "Yes" << endl;
}