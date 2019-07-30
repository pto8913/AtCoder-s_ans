#include<iostream>
#include<vector>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int N, M;
  cin >> N >> M;
  vector<pair<int,int>> LR(M);
  rep(i,M) cin >> LR[i].first >> LR[i].second;
  int Lm = 0, Rm = N+1;
  rep(i,M){
    Lm = max(LR[i].first, Lm);
    Rm = min(LR[i].second, Rm);
  }
  cout << max(0, Rm-Lm+1) << endl;    
}
