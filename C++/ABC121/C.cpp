#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef pair<Int,Int> P;

#define rep(i,n) for(int i=0;i<n;++i)
#define mp(a,b) make_pair(a,b)
#define srt(a, b) sort(a.begin(), a.end(), b)

bool cmp(const P& a, const P& b){
  return a.first < b.first;
}

int main(){
  Int N, M, ans = 0;
  cin >> N >> M;
  vector<P> A(N);
  rep(i,N) cin >> A[i].first >> A[i].second;
  srt(A,cmp);
  for (auto& x: A){
    Int l = x.first, r = x.second;
    if (r <= M) { ans += r*l; M -= r;}
    else if (r > M) { ans += M*l; break; }
  }
  cout << ans << endl;
}
