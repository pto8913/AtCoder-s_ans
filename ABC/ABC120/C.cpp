#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  string s;
  cin >> s;

  int NumOfZero = 0, NumOfOne = 0;
  rep(i, 0, s.length())
  {
    if (s[i] == '0') ++NumOfZero;
    else ++NumOfOne;
  }
  
  cout << (NumOfOne < NumOfZero ? NumOfOne : NumOfZero) * 2 << endl;
}