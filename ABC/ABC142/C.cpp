#include <iostream>
#include <unordered_map>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, x;
  cin >> n;
  unordered_map<int, int> v;
  rep(i, 0, n) {
    cin >> x;
    v[x] = i+1;
  }
  rep(i, 0, n) {
    cout << v[i+1] << endl;
  }
}