#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  cin >> n;

  int items[10];
  int a, b, c;
  int count = 0;
  rep(i, 0, n)
  {
    cin >> a >> b >> c;
    --a; --b; --c;

    ++items[a];
    ++items[b];
    ++items[c];
  }

  int tmp = 0;
  rep(i, 0, 10)
  {
    count += items[i]/2;
    tmp += items[i]%2;
  }
  cout << count + tmp /4 << endl;
}