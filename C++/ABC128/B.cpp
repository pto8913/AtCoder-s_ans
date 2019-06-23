#include<iostream>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

typedef pair<string, int> P;

bool cmp(P &a, P &b){
  return a.first < b.first || a.first == b.first && a.second > b.second;
}

int main(){
  int N;
  cin >> N;
  vector<P> SP(N);
  rep(i,N) cin >> SP[i].first >> SP[i].second;
  vector<P> CSP = SP;
  sort(CSP.begin(), CSP.end(), cmp);
  rep(i,N) {
    rep(j,N){
      if (CSP[i] == SP[j]) {
        cout << j+1 << endl;
        break;
      }
    }
  }
}
