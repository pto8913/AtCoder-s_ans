#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

bool check(const int in)
{
  return in - 1 >= 0;
}

bool check(vector<int>& Vec, const int A, const int B, const int C, const int NumOf)
{
  if (NumOf == 1)
  {
    if (check(Vec[A]) == true)
    {
      --Vec[A];
      return true;
    }
  }

  if (NumOf == 2) 
  {
    if (check(Vec[A]) == true && check(Vec[B]) == true)
    {
      --Vec[A]; --Vec[B];
      return true;
    }
  }
  
  if (NumOf == 3) 
  {
    if (check(Vec[A]) == true && check(Vec[B]) == true && check(Vec[C]) == true)
    {
      --Vec[A]; --Vec[B]; --Vec[C];
      return true;
    }
  }
  return false;
}

int main(){
  int t;
  cin >> t;

  int a, b, c;
  rep(i, 0, t)
  {
    cin >> a >> b >> c;
    vector<int> vec = {a, b, c};
    sort(vec.begin(), vec.end());
    int ans = 0;
    ans += check(vec, 0, 0, 0, 1);
    ans += check(vec, 1, 0, 0, 1);
    ans += check(vec, 2, 0, 0, 1);
    ans += check(vec, 1, 2, 0, 2);
    ans += check(vec, 0, 2, 0, 2);
    ans += check(vec, 0, 1, 0, 2);
    ans += check(vec, 0, 1, 2, 3);
    cout << ans << endl;
  }
}