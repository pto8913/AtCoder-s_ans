#include<iostream>
#include<vector>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int N, M;
  cin >> N >> M;
  vector<vector<int>> S(M);
  rep(i,M) {
    int k;
    cin >> k;
    S[i].resize(k);
    rep(j,k){
      cin >> S[i][j];
      --S[i][j];
    }
  }
  
  vector<int> P(M);
  rep(i,M) cin >> P[i];
  int ans = 0;
  rep(i, 1<<N){
    bool ok = true;
    rep(j,M){
      int x = 0;
      rep(k,S[j].size()) if ((i >> S[j][k] & 1)) ++x;
      x %= 2;
      if (x != P[j]) ok = false;
    }
    if (ok) ++ans;
  }
  cout << ans << endl;          
}
