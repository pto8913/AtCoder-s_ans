#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, k, h, cnt = 0;
  cin >> n >> k;
  rep(i, 0, n) {
    cin >> h;
    if (h >= k) ++cnt;
  }
  cout << cnt << endl;
}