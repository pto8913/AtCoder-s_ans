#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int N, Q, ac = 0;
  string S;
  cin >> N >> Q >> S;
  vector<int> vec(N);
  rep(i,N-1) {
    if(S[i] == 'A' && S[i+1] == 'C') ++ac;
    vec[i+1] = ac;
  }
  rep(i,Q){
    int l, r;
    cin >> l >> r;
    cout << vec[r-1] - vec[l-1] << endl;
  }
}
