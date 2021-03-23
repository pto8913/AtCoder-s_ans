#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i=a; i<(n); ++i)
typedef long long ll;

struct edge {
    int to;
};

typedef pair<int, int> P; 

int V, d[MAX_V];
vector<edge> G[MAX_V]; 

void dijkstra(int s) {
    fill(d, d + V, INF);
    d[s] = 0;  

    priority_queue<P, vector<P>, greater<P>> que;  
    que.push(P(0, s));
    while (!que.empty()) {
        P p = que.top();
        que.pop();
        int v = p.second; 
        if (d[v] < p.first) {
            continue;
        }
        for (auto e : G[v]) {
            if (d[e.to] > d[v] + 1) {
                d[e.to] = d[v] + 1;
                que.push(P(d[e.to], e.to));
            }
        }
    }
}
int main()
{
    int n, x, y;
    cin >> n >> x >> y;

    
}