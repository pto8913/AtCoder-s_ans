#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  string s;
  cin >> s;
  int len = s.length();

  string ans = "", tmp = "";
  bool pass = false;
  rep(i, 0, len)
  {
    if (pass) {
      pass = false;
      continue;
    }
    if (i != len - 1)
    {
      if (s[i] == 'a' && s[i+1] == 'o')
      {
        ans += "ki";
        pass = true;
      }
      else
      {
        ans += s[i];
      }
    }
    else
    {
      ans += s[i];
    }
  }
  cout << ans << endl;
}