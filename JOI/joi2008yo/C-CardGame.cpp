#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); ++i)
#define gsort(a) sort(a.begin(), a.end(), greater<int>())

typedef vector<int> vi;

void f(vi &a, int &ba){
  int res = 0, i = 0, d = -1;
  for (auto x : a){
    if (ba < x){
      if (res == 0){
        res = x;
        d = i;
      }else if(res > x){
        res = x;
        d = i;
      }
    }
    ++i;
  }
  if (d != -1){
    a.erase(a.begin() + d);
  }
  ba = res;
}

int main(){
  int n, v, ba = 0;
  cin >> n;

  vector<bool> t(n*2);
  rep(i, n) {
    cin >> v;
    t[v-1] = true;
  }

  vi taro, hana;
  rep(i, n*2){
    if (t[i]) taro.push_back(i+1);
    else hana.push_back(i+1);
  }
  gsort(taro);
  gsort(hana);

  int x = 0;
  while(true){
    if (taro.size() == 0 || hana.size() == 0) break;
    if (x % 2 == 0){
      if (ba == 0){
        ba = taro.back();
        taro.pop_back();
      }else{
        f(taro, ba);
      }
    }else{
      if (ba == 0){
        ba = hana.back();
        hana.pop_back();
      }else{
        f(hana, ba);
      }
    }
    ++x;
  }

  cout << hana.size() << endl;
  cout << taro.size() << endl;
}
