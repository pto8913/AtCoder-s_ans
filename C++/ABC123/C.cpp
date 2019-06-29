#include <iostream>

using namespace std;

int main(){
  long long N, A, B, C, D, E;
  cin >> N >> A >> B >> C >> D >> E;
  long long x = min(A, min(B, min(C, (min(D, E)))));
  cout << (N + (x-1))/x + 4 << endl;
}
