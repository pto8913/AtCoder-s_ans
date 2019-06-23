#include <iostream>

using namespace std;

int main(){
  int P, Q, R;
  cin >> P >> Q >> R;
  cout << min(P+Q, min(Q+R, P+R)) << endl;  
}
