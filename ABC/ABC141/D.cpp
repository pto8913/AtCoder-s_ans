#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define ll long long

int main(){
  int n, m;
  cin >> n >> m;
  vector<ll> a(n);
  priority_queue<int> que;
  rep(i, 0, n) {
    cin >> a[i];
    que.push(a[i]);
  }
  int x;
  rep(i, 0, m) {
    x = que.top();
    que.pop();
    que.push(x / 2);
  }
  ll ans = 0;
  while (!que.empty()) {
    ans += que.top();
    que.pop();
  }
  cout << ans << endl;
}