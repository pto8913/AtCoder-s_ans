#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long Int;

#define rep(i, n) for(int i=0; i<n; ++i)
#define srt(A) sort(A.begin(), A.end(), greater<Int>())

int main(){
  Int X, Y, Z, K;
  cin >> X >> Y >> Z >> K;
  vector<Int> A(X), B(Y), C(Z), res;
  rep(i, X) cin >> A[i]; srt(A);
  rep(i, Y) cin >> B[i]; srt(B);
  rep(i, Z) cin >> C[i]; srt(C);
  
  rep(i, X){
    rep(j, Y){
      rep(k, Z){
        if ((i+1)*(j+1)*(k+1) <= K) res.push_back(A[i]+B[j]+C[k]);
        else break;
      }
    }
  }
  srt(res);
  rep(i,K)
    cout << res[i] << endl;
}
