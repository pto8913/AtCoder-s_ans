#include <iostream>

using namespace std;

int main(){
  char b;
  cin >> b;
  if (b == 'A') cout << 'T' << endl;
  else if (b == 'T') cout << 'A' << endl;
  else if (b == 'C') cout << 'G' << endl;
  else cout << 'C' << endl;
}
