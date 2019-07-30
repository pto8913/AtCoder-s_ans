#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, k;
	string S, ans;
	cin >> n >> S >> k;
	
	char select = S[k - 1];
	for (int i = 0; i < n; i++) {
		if (S[i] == select) {
			ans += S[i];
		}
		else {
			ans += "*";
		}
	}
	cout << ans << endl;
}
