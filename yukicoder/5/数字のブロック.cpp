#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int l, n;
  cin >> l >> n;
  vector<int> w(n);
  rep(i, 0, n) cin >> w[i];
  sort(w.begin(), w.end());
  int count = 0;
  rep(i, 0, n)
  {
    if (l-w[i] < 0) break;
    l -= w[i];
    ++count;
  }
  cout << count << endl;
}