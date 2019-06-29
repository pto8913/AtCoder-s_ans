#include "bits/stdc++.h"
using namespace std;

int main() {
	string s;
	cin >> s;

	int ans1 = 0, ans2 = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] - '0' == i % 2) ans1++;
		else ans2++;
	}
	cout << min(ans1, ans2) << endl;
}

/*
#include <iostream>
#include <string>

using namespace std;

#define rep(i, n) for(int i=0; i<n; ++i)

int main(){
  string S;
  cin >> S;
  int n = S.size();
  int A = 0, B = 0;
  rep(i, n){
    char c;
    if (i%2 == 0) c = '0';
    else c = '1';
    if (S[i] != c) ++A;
  }
  rep(i, n){
    char c;
    if (i%2 == 1) c = '0';
    else c = '1';
    if (S[i] != c) ++B;
  }
  cout << min(A, B) << endl;
}
*/
