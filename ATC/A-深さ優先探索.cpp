#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)
#define ll long long

int h, w;
char maze[505][505];
bool reach[505][505] = { false };

bool dfs(int x, int y) {
  if (x < 0 || y < 0 || x >= w || y >= h || maze[y][x] == '#') {
    return false;
  }
  if (reach[y][x]) {
    return false;
  }
  reach[y][x] = true;
  if (maze[y][x] == 'g') {
    return true;
  }
  return dfs(x+1, y) || dfs(x-1, y) || dfs(x, y+1) || dfs(x, y-1);
}

int main(){
  scanf("%d%d", &h, &w);

  int sx, sy;
  rep(y, 0, h) {
    rep(x, 0, w) {
      scanf("%c", &maze[y][x]);
      if (maze[y][x] == 's') {
        sx = x;
        sy = y;
      }
    }
  }

  if (dfs(sx, sy)) {
    printf("Yes");
  } else {
    printf("No");
  }
}