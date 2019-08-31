#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

char c[501][501];
bool reach[501][501] = { false };
int h, w;

bool dfs(int x, int y) {
  if (x < 0 || y < 0 || x >= w || y >= h || c[y][x] == '#') {
    return false;
  }
  if (reach[y][x]) {
    return false;
  }
  reach[y][x] = true;

  if (c[y][x] == 'g') {
    return true;
  }

  return dfs(x+1, y) || dfs(x, y+1) || dfs(x-1, y) || dfs(x, y-1);
}

int main(){
  cin >> h >> w;

  char tile;
  int start_x = 0, start_y = 0;
  rep(y, 0, h) {
    rep(x, 0, w) {
      cin >> tile;
      c[y][x] = tile;
      if (tile == 's') {
        start_x = x;
        start_y = y;
      }
    }
  }
  if (dfs(start_x, start_y)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}