#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)

vector<int> v[200005];
int ans[200005];

void f(int cur, int par, int value) {
  ans[cur] += value;
  for (auto e : v[cur]) {
    if (e == par) {
      continue;
    }
    f(e, cur, ans[cur]);
  }
}

int main(){
  int n, q, a, b, p, x;
  cin >> n >> q;

  rep(i, n-1) {
    cin >> a >> b;
    v[a-1].push_back(b-1);
    v[b-1].push_back(a-1);
  }
  
  rep(i, q) {
    cin >> p >> x;
    ans[p-1] += x;
  }

  f(0, -1, 0);
  rep(i, n) {
    cout << ans[i] << endl;
  }
}