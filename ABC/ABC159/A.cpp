#include <iostream>
#include <vector>

using namespace std;

#define rep(i, a, n) for(int i=a; i<(n); ++i)
typedef long long ll;

std::vector<std::vector<long long>> comb(int n, int r) {
  std::vector<std::vector<long long>> v(n + 1,std::vector<long long>(n + 1, 0));
  for (int i = 0; i < v.size(); i++) {
    v[i][0] = 1;
    v[i][i] = 1;
  }
  for (int j = 1; j < v.size(); j++) {
    for (int k = 1; k < j; k++) {
      v[j][k] = (v[j - 1][k - 1] + v[j - 1][k]);
    }
  }
  return v;
}

int main()
{
    int n, m;
    cin >> n >> m;
  	vector<vector<ll>> a = comb(n, 2);
    vector<vector<ll>> b = comb(m, 2);
	if (n < 2 && m < 2) 
    {
      cout << 0 << endl;
    }
  	else if (n >= 2 && m >= 2)
    {
      cout << a.size() + b.size() << endl;
    }
  	else if (n < 2)
    {
      cout << b.size() << endl;
    }
  	else if (m < 2)
    {
      cout << a.size() << endl;
    }
}