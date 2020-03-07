#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  string s;
  cin >> s;

  int Count = 0;
  int Ans = 0;
  string Prev = "";
  rep(i, 0, s.length())
  {
    if (i == 0) Prev = s[i];
    if (s[i] == 'A' || s[i] == 'C' || s[i] == 'G' || s[i] == 'T')
    {
      if (Prev == 'A' || Prev == 'C' || Prev == 'G' || Prev == 'T') ++Count;
      else 
      {
        if (Ans < Count) 
        {
          Ans = Count;
          Count = 0;
        }
      }
    }
    Prev = s[i];
  }
  cout << Ans << endl;
}