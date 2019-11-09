// Result is TLE........... Wrong Answer
// I can't solve

#include <iostream>
#include <vector>
#include <queue>
#include <cstdio>
#include <map>
using namespace std;
const long long INF = 1LL<<60;

#define Pdi pair<double, int>
#define Pid pair<int, double>
#define mkp(a, b) make_pair(a, b)
#define ll long long
#define rep(i, a, n) for(int i = a; i < (n); ++i)

struct Graph {
  Graph(int size) : adj(size, vector<Pid>()) { this-> n = size; }

  void addEdge(int a, int b, double w) {
    adj[a].push_back(mkp(b, w));
  }

  void dijkstra(int a) {
    d = vector<double>(n, INF);
    d[a] = 0;
    priority_queue<Pdi, vector<Pdi>, greater<Pdi>> que;
    que.push(mkp(0, a));

    while (!que.empty()) {
      int u = que.top().second;
      que.pop();

      for (auto i: adj[u]) {
        if (d[i.first] > d[u] + i.second) {
          d[i.first] = d[u] + i.second;
          que.push(mkp(d[i.first], i.first));
        }
      }
    }
  }

  double dist(int a) {
    return d[a];
  }

private:
  int n;
  vector<vector<Pid>> adj;
  vector<double> d;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, m, l, r, c;
    cin >> n >> m;
    Graph G(n);

    rep(i, 0, m){
        cin >> l >> r >> c;
        --l; --r;
        rep(j, l, r+1){
          G.addEdge(l, j, c);
        }
    }
    G.dijkstra(0);
    rep(i, 0, n+1){
      cout << G.dist(i) << endl;
    }
}