#include <bits/stdc++.h>

using namespace std;

int i;
int main() {
	int N, ans = 0;
	string S;
	cin >> N >> S;

	for (i = 0; i < N; i++) {
		if (S[i] == '.') {
			ans++;
		}
	}
	vector<int> v(N + 1);
	v[0] = ans;
	for (i = 1; i < N+1; i++) {
		if (S[i-1] == '#') {
			v[i] = v[i - 1] + 1;
		}
		else {
			v[i] = v[i - 1] - 1;
		}
	}
  	sort(v.begin(),v.end());
	cout << v[0] << endl;
}
