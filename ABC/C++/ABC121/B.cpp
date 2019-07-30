#include <iostream>
#include <vector>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int N, M, C;
  cin >> N >> M >> C;
  vector<int> B(M);
  rep(i,M) cin >> B[i];
  int ans = 0;
  rep(i,N){
    int point = 0;
    rep(j,M){
      int A;
      cin >> A;
      point += A*B[j];
    }
    if (point + C > 0) ++ans;
  }
  cout << ans << endl;
}
