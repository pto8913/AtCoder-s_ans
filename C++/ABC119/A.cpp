#include <iostream>
#include <string>

using namespace std;

int main(){
  string S, c = "2019/04/30";
  cin >> S;
  cout << (S <= c ? "Heisei" : "TBD") << endl;
}
