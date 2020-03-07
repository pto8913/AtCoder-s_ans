#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;

  int a, b, c, d;
  string e;
  vector<int> vec(10, 1);
  rep(i, 0, n)
  {
    cin >> a >> b >> c >> d >> e;
    
    if (e == "YES")
    {
      ++vec[a];
      ++vec[b];
      ++vec[c];
      ++vec[d];
    }
    else
    {
      --vec[a];
      --vec[b];
      --vec[c];
      --vec[d];
    }
  }

  int Max = 0;
  int ans = 0;
  rep(i, 0, 10)
  {
    if (Max < vec[i])
    {
      Max = vec[i];
      ans = i;
    }
  }
  cout << ans << endl;
}