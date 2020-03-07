#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, m;
  cin >> n >> m;
  bool cup[3] = { false };
  int p, q;
  cup[n-1] = true;
  rep(i, 0, m)
  {
    cin >> p >> q;
    --p; --q;
    bool tmp = cup[q];
    cup[q] = cup[p];
    cup[p] = tmp;
  }
  rep(i, 0, 3)
  {
    if (cup[i] == true) cout << i+1 << endl;
  }
}