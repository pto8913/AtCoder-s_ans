#include <iostream>
#include <vector>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int N, A, B, C;
int v[8];

int dfs(int x, int a, int b, int c){
  if (x == N){
    if (a == 0 || b == 0 || c == 0) return 1e9;
    return abs(a - A) + abs(b - B) + abs(c - C);
  }
  int ret = 1e9;
  ret = min(ret, dfs(x + 1, a, b, c));
  ret = min(ret, dfs(x + 1, a + v[x], b, c) + 10);
  ret = min(ret, dfs(x + 1, a, b + v[x], c) + 10);
  ret = min(ret, dfs(x + 1, a, b, c + v[x]) + 10);
  return ret;
}

int main(){
  cin >> N >> A >> B >> C;
  rep(i, 8) cin >> v[i];
  cout << dfs(0, 0, 0, 0) - 30 << endl;
}
