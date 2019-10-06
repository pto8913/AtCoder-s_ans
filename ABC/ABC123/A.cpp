#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(void){
  int a, b, c, d, e, k;
  cin >> a >> b >> c >> d >> e >> k;
  string ans = ":(";
  if(e-a <= k){
    ans = "Yay!";
  }
  cout << ans << endl;
}
