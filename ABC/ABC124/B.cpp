#include "bits/stdc++.h"
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> h(n);
	for (int i = 0; i < n; i++) cin >> h[i];
	
	int ans = 0;
	int max_height = -1;

	for (int i = 0; i < n; i++) {
		if (max_height <= h[i]) {
			ans += 1;
			max_height = h[i];
		}

	}
	cout << ans << endl;	
}
/*
#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i<n; ++i)

int main(){
  int N, ans = 1;
  cin >> N;
  vector<int> H(N);
  rep(i, N) cin >> H[i];

  for (int i = 1; i < N; ++i){
    int cnt = 0;
    rep(j, i+1){
      if (H[j] <= H[i]){
        cnt++;
      }
    }
    if (cnt == i+1){
      ans++;
    }
  }
  cout << ans << endl;
}
*/
