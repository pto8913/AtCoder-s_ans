#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  string s;
  cin >> s;
  int len = s.length();
  string ans = "";
  rep(i, 0, len)
  {
    ans += ((s[i] - '0') - i-1) % 64 + '0';
  }
  cout << ans << endl;
}