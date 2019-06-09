#include "bits/stdc++.h"

using namespace std;
const long long mod = 1e9+7;

int main(){
  int N, M;
  cin >> N >> M;
  vector<bool> check(N+1, true);
  for (int i = 0; i < M; i++) {
    int a;
    cin >> a;
    check[a] = false;
  }

  vector<long long int> dp(N+1);
  dp[0] = 1;
  for (int i = 0; i < N; i++){
    for (int j = i+1; j <= min(N, i+2); j++){
      if (check[j]){
        dp[j] += dp[i];
        dp[j] %= mod;
      }
    }
  }

  cout << dp[N] << endl;
}
