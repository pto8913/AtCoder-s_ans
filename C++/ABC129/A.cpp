#include <iostream>

#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

int main(){
  int P, Q, R;
  cin >> P >> Q >> R;
  cout << min(P+Q, min(Q+R, P+R)) << endl;  
}
