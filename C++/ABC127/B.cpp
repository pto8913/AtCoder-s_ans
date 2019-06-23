#include<iostream>

using namespace std;

#define rep(i,n) for(int i=0;i<n;++i)

int main(){
  int r, D, x;
  cin >> r >> D >> x;
  rep(i,10){
    int tmp = r*x-D;
  	cout << tmp << endl;
    x = tmp;
  }
}
