#include <iostream>
using namespace std;

int main(){
  int a,b;
  cin >> a >> b;
  int ans = 0;
  
  cout << max(a+b, max(a*2-1, b*2-1)) << endl;
}
