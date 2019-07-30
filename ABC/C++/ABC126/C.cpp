#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	double p = 0.0;

	for (int i = 1; i <= N; i++) {
		int cnt = 0;
		int tmp = i;
		while (tmp < K) {
			tmp *= 2;
			cnt++;
		}
		p += 1.0 / N * (1.0 / pow(2, cnt));
	}
	printf("%0.12lf\n", p);
}
