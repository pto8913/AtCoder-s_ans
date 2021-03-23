#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int h, w;
char c[500][500];
bool reach[500][500] = {false};

bool DFS(int x, int y)
{
  if (x >= w || y >= h || x < 0 || y < 0) return false;
  if (c[y][x] == '#' || reach[y][x] == true) return false;
  if (c[y][x] == 'g') return true;
  reach[y][x] = true;
  return DFS(x+1, y) || DFS(x-1, y) || DFS(x, y+1) || DFS(x, y-1);
}

int main(){
  cin >> h >> w;

  int StartX = 0, StartY = 0;
  rep(y, 0, h)
  {
    rep(x, 0, w)
    {
      cin >> c[y][x];
      if (c[y][x] == 's')
      {
        StartX = x;
        StartY = y;
      }
    }
  }
  bool res = DFS(StartX, StartY);
  if (res) cout << "Yes" << endl;
  else cout << "No" << endl;
}