#include "bits/stdc++.h"
using namespace std;
const int K = 2005;
int N, M, U[K][K], D[K][K], L[K][K], R[K][K];
char S[K][K];
int main(){
  scanf("%d%d", &N, &M);
  for (int i = 1; i <= N; i++) { scanf("%s", S[i]+1); }
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      if (S[i][j] == '.') {
        U[i][j] = U[i-1][j] + 1;
        L[i][j] = L[i][j-1] + 1;
      }
    }
  }
  for (int i = N; i >= 1; i--) {
    for (int j = M; j >= 1; j--) {
      if (S[i][j] == '.') {
        D[i][j] = D[i+1][j] + 1;
        R[i][j] = R[i][j+1] + 1;
      }
    }
  }
  int ans = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      if (S[i][j] == '.') {
        ans = max(ans, U[i][j]+D[i][j]+L[i][j]+R[i][j]-3);
      }
    }
  }
  cout << ans << endl;
}
