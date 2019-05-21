#include <iostream>
#include <string>

using namespace std;

int main() {
	int S, left, right;
	cin >> S;
	left = S / 100;
	right = S % 100;

	string ans = "NA";
	if ((left > 0 && left < 13) && (right > 0 && right < 13)){
		ans = "AMBIGUOUS";
	}
	else if (right >= 0 && (left > 0 && left < 13)) {
		ans = "MMYY";
	}
	else if (left >= 0 && (right > 0 && right < 13)) {
		ans = "YYMM";
	}

	cout << ans << endl;
}
