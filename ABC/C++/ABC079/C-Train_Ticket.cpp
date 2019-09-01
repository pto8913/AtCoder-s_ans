#include <iostream>
#include <string>

using namespace std;

#define rep(i, a, n) for(int i = a; i < (n); ++i)

int main(){
  char s[4];
  scanf("%s", s);

  int ans = 0;
  rep(bit, 0, 1 << 3) {
    int tmp = s[0] - '0';
    string stmp;
    stmp += s[0];
    rep(j, 0, 3) {
      if ((bit >> j) & 1) {
        tmp -= s[j+1] - '0';
        stmp += '-';
      } else {
        tmp += s[j+1] - '0';
        stmp += '+';
      }
      stmp += s[j+1];
    }
    if (tmp == 7) {
      printf("%s=7\n", stmp.c_str());
      exit(0);
    }
  }
}