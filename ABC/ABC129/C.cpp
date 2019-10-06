#include <iostream>
#include <vector>

#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;
const long long mod = 1e9+7;

int main(){
  int N, M;
  cin >> N >> M;
  vector<int> W(M), dp(N+1);
  rep(i,M) {
    cin >> W[i];
    dp[W[i]] = -1;
  }
  dp[0] = 1;
  for(int i = 1; i <= N; ++i){
    if (dp[i] == -1) continue;
    if (i >= 2 && dp[i-2] != -1) {
      dp[i] += dp[i-2] % mod;
    }
    if (dp[i-1] != -1){
      dp[i] += dp[i-1] % mod;
    }
  }
  cout << dp[N] % mod << endl;
}
