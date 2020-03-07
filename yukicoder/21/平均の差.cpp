#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n, k;
  cin >> n >> k;
  vector<int> vec(n);
  rep(i, 0, n) cin >> vec[i];

  sort(vec.begin(), vec.end());

  cout << vec[n-1] - vec[0] << endl;
}