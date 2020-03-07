#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

const long long MOD = (long long)1e9+7;
vector<vector<long long>> comb(int n, int r) {
  vector<vector<long long>> v(n + 1,vector<long long>(n + 1, 0));
  for (int i = 0; i < v.size(); i++) {
    v[i][0] = 1;
    v[i][i] = 1;
  }
  for (int j = 1; j < v.size(); j++) {
    for (int k = 1; k < j; k++) {
      v[j][k] = (v[j - 1][k - 1] + v[j - 1][k]);
    }
  }
  return v;
}

int main(){
  long long n, a, b;
  cin >> n >> a >> b;

  long long tmp = pow(2, n);
  
} 