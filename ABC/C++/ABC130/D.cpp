#include <iostream>
#include <vector>

using namespace std;

int main(){
  long long N, K, ans = 0;
  cin >> N >> K;
  vector<long long> A(N);
  for (int i = 0; i < N ; ++i) { 
    cin >> A[i];
  }
  long long sum = 0;
  int right = 0;
  for (int left = 0; left < N; ++left){
    sum += A[left];
    while (sum >= K){
      ans += N - left;
      sum -= A[right];
      ++right;
    }
  }
  cout << ans << endl;
}
