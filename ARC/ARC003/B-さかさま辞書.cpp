#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  int n;
  scanf("%d", &n);

  vector<string> s(n);
  rep(i, 0, n) {
    string x;
    cin >> x;
    reverse(x.begin(), x.end());
    s[i] = x;
  }
  sort(s.begin(), s.end());
  for (auto ss : s) {
    reverse(ss.begin(), ss.end());
    cout << ss << endl;
  }
}