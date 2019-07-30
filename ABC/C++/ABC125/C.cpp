#include "bits/stdc++.h"

using namespace std;

int i;

int gcd(int x, int y){
  if (y == 0) return x;
  return gcd(y, x%y);
}

int main(){
  int N;
  cin >> N;
  vector<int> A(N), L(N), R(N);
  for (i = 0; i < N; i++){
    cin >> A[i]; 
  }
  for (i = 0; i < N-1; i++){
    L[i+1] = gcd(L[i], A[i]);
  }
  for (i = N-1; i >= 1; i--){
    R[i-1] = gcd(R[i], A[i]);
  }
  int ans = 0;
  for (i = 0; i < N; i++){
    ans = max(ans, gcd(L[i], R[i]));
  }
  cout << ans << endl;
}
