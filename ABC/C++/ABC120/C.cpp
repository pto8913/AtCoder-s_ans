#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
  string S;
  cin >> S;
  int red = count(S.cbegin(), S.cend(), '0');
  int blue = count(S.cbegin(), S.cend(), '1');
  cout << min(red*2, blue*2) << endl;
}
