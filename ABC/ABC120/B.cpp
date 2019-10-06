#include <iostream>
#include <vector>

using namespace std;

#define rep1(i,n) for(int i=1;i<=n;++i)

int main(){
  int A, B, K;
  cin >> A >> B >> K;
  vector<int> v;
  rep1(i,max(A,B+1)){
    if (A%i == 0 && B%i == 0){
      v.push_back(i);
    }
  }
  cout << v[v.size()-K] << endl;
}
