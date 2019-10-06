#include <iostream>
#include <vector>

#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> W(N);
  rep(i,N) cin >> W[i];
  int ans = (int)1e9+7;
  rep(T,N){
    int left = 0, right = 0;
    for(int i = 0; i<T; ++i){
      left += W[i];
    }
    for (int i = T; i<N; ++i){
      right += W[i];
    }
    ans = min(ans, abs(right-left));
  }
  cout << ans << endl;
}
