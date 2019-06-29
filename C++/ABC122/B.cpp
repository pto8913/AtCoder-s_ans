#include <iostream>
#include <string>

using namespace std;

int main(){
  string S;
  cin >> S;
  int i = 0, ans = 0, l = 0;
  while (S[i] != '\0'){
    if (S[i] != 'A' && S[i] != 'C' && S[i] != 'G' && S[i] != 'T') l = 0;
    else {
      ++l;
      ans = max(l, ans);
    }
    ++i;
  }
  cout << ans << endl;
}
