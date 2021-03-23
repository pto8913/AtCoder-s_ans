#include <iostream>
#include <queue>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

template<class T, class U>
struct P { 
    P(T InX, U InY) : X(InX), Y(InY) {};
    T X = 0; U Y = 0; 
};

const int dx[4] = { 1, -1, 0, 0 };
const int dy[4] = { 0, 0, 1, -1};

int main(){
    int R, C, Sy, Sx, Gy, Gx;
    cin >> R >> C >> Sy >> Sx >> Gy >> Gx;
    --Sy; --Sx; --Gy; --Gx;
    int dist[55][55];
    char graph[55][55];
    rep(y, 0, R)
    {
        rep(x, 0, C)
        {
            cin >> graph[y][x];
            dist[y][x] = -1;
        }
    }
    dist[Sy][Sx] = 0;

    queue<P<int, int>> q;
    q.push(P<int, int>(Sx, Sy));
    while (!q.empty())
    {
        P<int, int> p = q.front();
        q.pop();
        int x = p.X, y = p.Y;
        if (x == Gx && y == Gy) break;

        rep(i, 0, 4)
        {
            int nx = x + dx[i], ny = y + dy[i];
            if (graph[ny][nx] != '#' && dist[ny][nx] == -1)
            {
                q.push(P<int, int>(nx, ny));
                dist[ny][nx] = dist[y][x] + 1;
            }
        }
    }
    cout << dist[Gy][Gx] << endl;
}