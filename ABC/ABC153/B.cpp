#include <iostream>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  long long h;
  int n, a;
  cin >> h >> n;
  int Sum = 0;
  rep(i, 0, n) 
  {
    cin >> a;
    Sum += a;
  }

  if (Sum >= h)
  {
    cout << "Yes" << endl;
  }
  else
  {
    cout << "No" << endl;
  }
}