#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> P;
#define mp(a, b) make_pair(a, b)

bool cmp(const P& a, const P&b){
  if (a.second == 0 || b.second == 0) return false;
  return a.second < b.second;
}

int main(){
  int A, B, C, D, E;
  cin >> A >> B >> C >> D >> E;
  int a = A%10, b = B%10, c = C%10, d = D%10, e = E%10;
  vector<P> v{mp(A,a), mp(B,b), mp(C,c), mp(D,d), mp(E,e)};
  sort(v.begin(), v.end(), cmp);
  int ans = 0, i = 0;
  for (auto& x : v){
    if (i == 0){
      ans += x.first;
    }else{
      if (x.second == 0) ans += x.first;
      else ans += (x.first/10+1)*10;
    }
    ++i;
  }
  cout << ans << endl;
}
